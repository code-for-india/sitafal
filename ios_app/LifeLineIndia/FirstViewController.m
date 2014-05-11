#if !defined(__has_feature) || !__has_feature(objc_arc)
#error "This file requires ARC support."
#endif

#import "FirstViewController.h"
#import "AppDelegate.h"
#import "ReportViewController.h"



@interface FirstViewController () <GMSMapViewDelegate>
@end

@implementation FirstViewController {
    GMSMapView *_mapView;
    GMSGeocoder *_geocoder;
    BOOL firstLocationUpdate_;
}

- (IBAction) reportIncident:(id)sender {
    
    // take screenshot of the current view
    UIGraphicsBeginImageContext(self.view.bounds.size);
    [self.view.layer renderInContext:UIGraphicsGetCurrentContext()];
    UIImage *image = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    
    [AppDelegate appDelegate].mapImage = image;
    
    ReportViewController *reportController = (ReportViewController *)[self.storyboard instantiateViewControllerWithIdentifier:@"ReportNav"];
    
    [self presentViewController:reportController animated:YES completion:nil];
}

-(IBAction) incidentInfo:(id)sender {
    UIAlertView *alert = [[UIAlertView alloc]
                          initWithTitle:@"Reporting Instructions"
                          message:@"Please upload one or more pictures along with quality of facilities at school"
                          delegate:nil
                          cancelButtonTitle:@"OK"
                          otherButtonTitles:nil];
    [alert show];
}


- (void)viewDidLoad {
    [super viewDidLoad];
    
    
    GMSCameraPosition *camera = [GMSCameraPosition cameraWithLatitude:12.9667
                                                            longitude:77.5667
                                                                 zoom:16];
    _mapView = [GMSMapView mapWithFrame:CGRectZero camera:camera];
    [_mapView setMinZoom:10 maxZoom:18];
    _mapView.settings.myLocationButton = YES;
    _mapView.settings.compassButton = YES;
    
    _mapView.delegate = self;
    [_mapView addObserver:self forKeyPath:@"myLocation" options:NSKeyValueObservingOptionNew context:NULL];
    
    _geocoder = [[GMSGeocoder alloc] init];
    
    self.view = _mapView;
    
    dispatch_async(dispatch_get_main_queue(), ^{
        _mapView.myLocationEnabled = YES;
    });
}

-(void) dealloc {
    [_mapView removeObserver:self
                  forKeyPath:@"myLocation"
                     context:NULL];
}


-(void) observeValueForKeyPath:(NSString *)keyPath
                      ofObject:(id)object
                        change:(NSDictionary *)change
                       context:(void *)context {
    if(!firstLocationUpdate_) {
        firstLocationUpdate_ = YES;
        
        CLLocation *location = [change objectForKey:NSKeyValueChangeNewKey];
        _mapView.camera = [GMSCameraPosition cameraWithTarget:location.coordinate zoom:16];
        
        [self mapView:_mapView didLongPressAtCoordinate:location.coordinate];
    }
}


#pragma mark - GMSMapViewDelegate

- (void)mapView:(GMSMapView *)mapView
didLongPressAtCoordinate:(CLLocationCoordinate2D)coordinate {
    
    //[_mapView clear];
    [AppDelegate appDelegate].incidentLocation = coordinate;
    
    // On a long press, reverse geocode this location.
    GMSReverseGeocodeCallback handler = ^(GMSReverseGeocodeResponse *response, NSError *error) {
        
        GMSAddress *address = response.firstResult;
        NSString *addressStr = [address.lines componentsJoinedByString:@"\n"];
        
        AppDelegate *ad = [AppDelegate appDelegate];
        ad.incidentAddress = addressStr;
        
        if (address) {
            NSLog(@"Geocoder result: %@", address);
            
            GMSMarker *marker = [GMSMarker markerWithPosition:address.coordinate];
            
            marker.title = address.thoroughfare;
            [ad.formData setValue:address.thoroughfare forKey:@"address"];
            
            NSMutableString *snippet = [[NSMutableString alloc] init];
            if (address.subLocality != NULL) {
                [snippet appendString:[NSString stringWithFormat:@"%@\n",
                                       address.subLocality]];
            }
            if (address.locality != NULL) {
                [snippet appendString:[NSString stringWithFormat:@"%@\n",
                                       address.locality]];
            }
            if (address.administrativeArea != NULL) {
                [snippet appendString:[NSString stringWithFormat:@"%@\n",
                                       address.administrativeArea]];
            }
            if (address.country != NULL) {
                [snippet appendString:[NSString stringWithFormat:@"%@\n",
                                       address.country]];
            }
            
            double lat = coordinate.latitude;
            double lon = coordinate.longitude;
            
            [ad.formData setValue:[NSString stringWithFormat:@"%f", lat] forKey:@"lat"];
            [ad.formData setValue:[NSString stringWithFormat:@"%f", lon] forKey:@"lon"];
            
            [ad.formData setValue:address.addressLine1 forKey:@"address"];
            [ad.formData setValue:address.locality forKey:@"city"];
            [ad.formData setValue:address.administrativeArea forKey:@"state"];
            [ad.formData setValue:address.country forKey:@"country"];
            [ad.formData setValue:address.postalCode forKey:@"pin"];
            
            NSLog(@"....data...\n%@", ad.formData);
            
            marker.snippet = addressStr;
            marker.appearAnimation = kGMSMarkerAnimationPop;
            mapView.selectedMarker = marker;
            marker.map = _mapView;
            
            // center the map w.r.t selected coordinates
            // _mapView.camera = [GMSCameraPosition cameraWithTarget:coordinate zoom:_mapView.camera.zoom];
            [_mapView animateToLocation:coordinate];

        } else {
            NSLog(@"Could not reverse geocode point (%f,%f): %@",
                  coordinate.latitude, coordinate.longitude, error);
        }
    };
    [_geocoder reverseGeocodeCoordinate:coordinate completionHandler:handler];
}

@end
