//
//  ReportViewController.h
//

#import <UIKit/UIKit.h>
#import <Firebase/Firebase.h>
#import "FormViewController.h"

@interface ReportViewController : UIViewController<FormViewControllerDelegate>

@property (nonatomic,retain) IBOutlet UISegmentedControl *segmentControl;

-(IBAction) sendReport:(id)sender;
-(IBAction) closeView:(id)sender;
-(IBAction) segmentSwitch:(id)sender;


@end
