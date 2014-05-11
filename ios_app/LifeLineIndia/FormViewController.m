//
//  FormViewController.m
//  SITA
//
//

#import "FormViewController.h"
#import "AppDelegate.h"
#import "TPKeyboardAvoidingScrollView.h"
#import "UIScrollView+TPKeyboardAvoidingAdditions.h"


@interface FormViewController ()

@end

@implementation FormViewController

// school info
@synthesize schoolName, schoolAddress, schoolCity,
            schoolTaluk, schoolDistrict, schoolState, schoolPin,
            reportersName, reportersPhone;

// entry access
@synthesize entry1, entry2a,entry2b, entry2c, entry2d, entry3;

// toilet condition
@synthesize toilet1, toilet2a, toilet2b, toilet3a, toilet3b, toilet3c, toilet3d, toilet4;

// drinking water
@synthesize water1, water2a, water2b, water2c, water3;

// playground
@synthesize ground1, ground2a, ground2b, ground2c, ground3;

// library
@synthesize library1, library2a, library2b, library2c, library2d, library3;

// upload photos
@synthesize btnCamera, btnAlbum,lblStatus, imageView;

@synthesize  delegate;


-(IBAction) nextForm:(id)sender {
    
    int curForm = [AppDelegate appDelegate].currentForm;
    NSMutableDictionary *formData = [AppDelegate appDelegate].formData;
    
    // school form info
    //
    if(curForm==FORM_SCHOOL_INFO) {
        [formData setValue:schoolName.text forKey:@"name"];
        [formData setValue:schoolAddress.text forKey:@"address"];
        [formData setValue:schoolCity.text forKey:@"city"];
        [formData setValue:schoolTaluk.text forKey:@"taluk"];
        [formData setValue:schoolDistrict.text forKey:@"district"];
        [formData setValue:schoolState.text forKey:@"state"];
        [formData setValue:schoolPin.text forKey:@"pin"];
        [formData setValue:reportersName.text forKey:@"repname"];
        [formData setValue:reportersPhone.text forKey:@"repphone"];
    }
    
    // entry/gate access
    //
    else if(curForm==FORM_ENTRY_ACCESS) {
        [formData setValue:entry1.isOn ? @"y":@"n"  forKey:@"entry1"];
        [formData setValue:entry2a.isOn ? @"y":@"n"  forKey:@"entry2a"];
        [formData setValue:entry2b.isOn ? @"y":@"n"  forKey:@"entry2b"];
        [formData setValue:entry2c.isOn ? @"y":@"n"  forKey:@"entry2c"];
        [formData setValue:entry2d.isOn ? @"y":@"n"  forKey:@"entry2d"];
        [formData setValue:entry3.isOn ? @"y":@"n"  forKey:@"entry3"];
    }
    
    // toilets condition
    //
    else if(curForm==FORM_TOILETS) {
        [formData setValue:toilet1.isOn ? @"y":@"n"  forKey:@"toilet1"];
        [formData setValue:toilet2a.isOn ? @"y":@"n"  forKey:@"toilet2a"];
        [formData setValue:toilet2b.isOn ? @"y":@"n"  forKey:@"toilet2b"];
        [formData setValue:toilet3a.isOn ? @"y":@"n"  forKey:@"toilet3a"];
        [formData setValue:toilet3b.isOn ? @"y":@"n"  forKey:@"toilet3b"];
        [formData setValue:toilet3c.isOn ? @"y":@"n"  forKey:@"toilet3c"];
        [formData setValue:toilet3d.isOn ? @"y":@"n"  forKey:@"toilet3d"];
        [formData setValue:toilet4.isOn ? @"y":@"n"  forKey:@"toilet4"];
    }
    
    // drinking water condition
    //
    else if(curForm==FORM_DRINKING_WATER) {
        [formData setValue:water1.isOn ? @"y":@"n"  forKey:@"water1"];
        [formData setValue:water2a.isOn ? @"y":@"n"  forKey:@"water2a"];
        [formData setValue:water2b.isOn ? @"y":@"n"  forKey:@"water2b"];
        [formData setValue:water2c.isOn ? @"y":@"n"  forKey:@"water2c"];
        [formData setValue:water3.isOn ? @"y":@"n"  forKey:@"water3"];
    }
    
    // playground condition
    //
    else if(curForm==FORM_PLAYFROUND) {
        [formData setValue:ground1.isOn ? @"y":@"n"  forKey:@"ground1"];
        [formData setValue:ground2a.isOn ? @"y":@"n"  forKey:@"ground2a"];
        [formData setValue:ground2b.isOn ? @"y":@"n"  forKey:@"ground2b"];
        [formData setValue:ground2c.isOn ? @"y":@"n"  forKey:@"ground2c"];
        [formData setValue:ground3.isOn ? @"y":@"n"  forKey:@"ground3"];
    }
    
    // library condition
    //
    else if(curForm==FORM_LIBRARY) {
        [formData setValue:library1.isOn ? @"y":@"n"  forKey:@"library1"];
        [formData setValue:library2a.isOn ? @"y":@"n"  forKey:@"library2a"];
        [formData setValue:library2b.isOn ? @"y":@"n"  forKey:@"library2b"];
        [formData setValue:library2c.isOn ? @"y":@"n"  forKey:@"library2c"];
        [formData setValue:library2d.isOn ? @"y":@"n"  forKey:@"library2d"];
        [formData setValue:library3.isOn ? @"y":@"n"  forKey:@"library3"];
    }

    NSLog(@"...form...data ... \n%@", formData);
    
    [self.delegate currentFormChanged:TRUE];
}

-(IBAction) prevForm:(id)sender {
    [self.delegate currentFormChanged:FALSE];
}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    
    // this info comes from map reverse-geocoding. so auto-fill the first form
    //
    
    AppDelegate *ad = [AppDelegate appDelegate];
    if(ad.currentForm==FORM_SCHOOL_INFO) {
        NSLog(@"....here....\n%@", ad.formData);
        self.schoolAddress.text = [ad.formData valueForKey:@"address"];
        self.schoolCity.text = [ad.formData valueForKey:@"city"];
        self.schoolState.text = [ad.formData valueForKey:@"state"];
        self.schoolPin.text = [ad.formData valueForKey:@"pin"];
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


- (IBAction) getCameraPicture:(id)sender {
    if (![UIImagePickerController isSourceTypeAvailable:UIImagePickerControllerSourceTypeCamera]) {
        UIAlertView *alert = [[UIAlertView alloc]
                              initWithTitle:@"No camera"
                              message:@"No camera found"
                              delegate:nil
                              cancelButtonTitle:@"Cancel"
                              otherButtonTitles:nil];
        [alert show];
        return;
    }
    UIImagePickerController *picker = [[UIImagePickerController alloc] init];
    picker.delegate = self;
    picker.allowsEditing = YES;
    picker.sourceType = UIImagePickerControllerSourceTypeCamera;
    [self presentViewController:picker animated:YES completion:nil];
}

- (IBAction) selectExistingPicture:(id)sender {
    if ([UIImagePickerController isSourceTypeAvailable:UIImagePickerControllerSourceTypePhotoLibrary]) {
        UIImagePickerController *picker = [[UIImagePickerController alloc] init];
        picker.delegate = self;
        picker.allowsEditing = YES;
        picker.sourceType = UIImagePickerControllerSourceTypePhotoLibrary;
        [self presentViewController:picker animated:YES completion:nil];
    }
    else {
        UIAlertView *alert = [[UIAlertView alloc]
                              initWithTitle:@"Error accessing photo library"
                              message:@"Device does not support a photo library"
                              delegate:nil
                              cancelButtonTitle:@"Cancel"
                              otherButtonTitles:nil];
        [alert show];
    }
}

////--------------------------------------
#pragma mark  - image picker delegates


- (void)imagePickerController:(UIImagePickerController *)picker
        didFinishPickingImage:(UIImage *)image
                  editingInfo:(NSDictionary *)editingInfo {
    [self uploadFile:image];
    self.imageView.image = image;
    [picker dismissModalViewControllerAnimated:YES];
}


- (void)imagePickerControllerDidCancel:(UIImagePickerController *)picker {
    
    [picker dismissViewControllerAnimated:YES completion:nil];
}



- (void)uploadFile:(UIImage *)image {
    
    //NSString *filepath = [[[NSBundle mainBundle] resourcePath] stringByAppendingPathComponent:@"login_form_bg.png"];
    //NSData *imageData = [NSData dataWithContentsOfFile:filepath];
    //NSLog(@"...image data size %d", imageData.length);
    
    NSString *incidentId = @"xxx123";
    NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
    formatter.dateFormat = @"yyyyMMddHHmmss";
    NSString *dateStr = [formatter stringFromDate:[NSDate date]];
    NSString *fileName = [NSString stringWithFormat:@"%@-%@.jpg", incidentId, dateStr];
    formatter = nil;
    
    NSLog(@"...final data...\n%@", [AppDelegate appDelegate].formData);
    
    NSMutableURLRequest *request = [[AFHTTPRequestSerializer serializer]
                                    multipartFormRequestWithMethod:@"POST"
                                    URLString:@"http://sita-india.appspot.com/realpost"
                                    parameters:[AppDelegate appDelegate].formData
                                    constructingBodyWithBlock:^(id<AFMultipartFormData> formData) {
                                        [formData appendPartWithFileData:UIImageJPEGRepresentation(image, 1.0) // max compression
                                                                    name:@"file"
                                                                fileName:fileName
                                                                mimeType:@"image/jpg"];
                                    } error:nil];
    
    AFURLSessionManager *manager = [[AFURLSessionManager alloc]
                                    initWithSessionConfiguration:[NSURLSessionConfiguration defaultSessionConfiguration]];
    NSProgress *progress = nil;
    lblStatus.text = @"Uploading photos...";
    
    NSURLSessionUploadTask *uploadTask = [manager uploadTaskWithStreamedRequest:request progress:&progress completionHandler:^(NSURLResponse *response, id responseObject, NSError *error) {
        if (error) {
            NSLog(@"Error: %@", error);
        } else {
            NSLog(@"Success ..... %@ %@", response, responseObject);
        }
    }];
    
    // Observe fractionCompleted using KVO
    [progress addObserver:self
               forKeyPath:@"fractionCompleted"
                  options:NSKeyValueObservingOptionNew
                  context:NULL];
    
    [uploadTask resume];
    
}

- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
{
    if ([keyPath isEqualToString:@"fractionCompleted"] && [object isKindOfClass:[NSProgress class]]) {
        NSProgress *progress = (NSProgress *)object;
        lblStatus.text = [NSString stringWithFormat:@"Upload status: %d%% completed", (int)progress.fractionCompleted * 100];
        [lblStatus setNeedsDisplay];
        return;
    }
    
    [super observeValueForKeyPath:keyPath ofObject:object change:change context:context];
}




@end
