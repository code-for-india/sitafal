//
//  AppDelegate.h
//
//

#import <UIKit/UIKit.h>
#import <GoogleMaps/GoogleMaps.h>

#define FORM_SCHOOL_INFO    0
#define FORM_ENTRY_ACCESS   1
#define FORM_TOILETS        2
#define FORM_DRINKING_WATER 3
#define FORM_PLAYFROUND     4
#define FORM_LIBRARY        5
#define FORM_UPLOAD_PHOTOS  6



@interface AppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;
@property (nonatomic, readwrite) CLLocationCoordinate2D incidentLocation;
@property (nonatomic, strong) NSString *incidentAddress;
@property (nonatomic, strong) UIImage *mapImage;
@property (nonatomic, readwrite) int currentForm;
@property(nonatomic, retain) NSMutableDictionary *formData;

+(AppDelegate *) appDelegate;

@end
