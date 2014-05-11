//
//  FormViewController.h
//  SITA
//
//

#import <UIKit/UIKit.h>
#import <MobileCoreServices/MobileCoreServices.h>
#import <SystemConfiguration/SystemConfiguration.h>

#import "AFNetworking.h"


@protocol FormViewControllerDelegate <NSObject>
- (void) currentFormChanged:(BOOL)next;
@end

@interface FormViewController : UIViewController<UINavigationControllerDelegate,UIImagePickerControllerDelegate>

// school information
@property(nonatomic,retain) IBOutlet UITextField *schoolName, *schoolAddress, *schoolCity,
                                        *schoolTaluk, *schoolDistrict, *schoolState, *schoolPin,
                                        *reportersName, *reportersPhone;

// entry access
@property(nonatomic,retain) IBOutlet UISwitch *entry1,
                                                *entry2a,*entry2b, *entry2c, *entry2d,
                                                *entry3;

// toilet condition
@property(nonatomic,retain) IBOutlet UISwitch *toilet1,
                                                *toilet2a, *toilet2b,
                                                *toilet3a, *toilet3b, *toilet3c, *toilet3d,
                                                *toilet4;
// drinking water
@property(nonatomic,retain) IBOutlet UISwitch *water1,
                                        *water2a, *water2b, *water2c,
                                        *water3;

// playground
@property(nonatomic,retain) IBOutlet UISwitch *ground1,
                                        *ground2a, *ground2b, *ground2c,
                                        *ground3;
// library
@property(nonatomic,retain) IBOutlet UISwitch *library1,
                                        *library2a, *library2b, *library2c, *library2d,
                                        *library3;



@property (nonatomic, weak) id<FormViewControllerDelegate> delegate;
@property(nonatomic,retain) IBOutlet UIButton *btnCamera;
@property(nonatomic,retain) IBOutlet UIButton *btnAlbum;
@property(nonatomic,retain) IBOutlet UILabel *lblStatus;
@property(nonatomic,retain) IBOutlet UIImageView *imageView;

- (void) uploadFile:(UIImage *)image;
- (IBAction) selectExistingPicture:(id)sender;
- (IBAction) getCameraPicture:(id)sender;


-(IBAction) nextForm:(id)sender;
-(IBAction) prevForm:(id)sender;


@end
