//
//  ReportViewController.m
//

#import "ReportViewController.h"
#import "AppDelegate.h"

#define CURRENT_VIEW 100

@interface ReportViewController ()

@end

@implementation ReportViewController {
    NSArray *controllers;
}

@synthesize segmentControl;

-(IBAction) closeView:(id)sender {
    [self dismissViewControllerAnimated:YES completion:nil];
}


// form delegate

-(void) currentFormChanged:(BOOL)next {
    int curForm = [AppDelegate appDelegate].currentForm;
    
    if(next) {
        if(curForm < 6) curForm += 1;
    }else {
        if(curForm >0) curForm -= 1;
    }

    [AppDelegate appDelegate].currentForm = curForm;
    [self.segmentControl setSelectedSegmentIndex:curForm];
    [self switchForm:curForm];
}

-(IBAction) sendReport:(id)sender {
    NSLog(@".....reporting...\n%@", [AppDelegate appDelegate].formData );
    
    [self dismissViewControllerAnimated:YES completion:nil];
}


- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

-(IBAction) segmentSwitch:(id)sender {
    UISegmentedControl *sc = (UISegmentedControl *)sender;
    NSInteger selectedSegment = sc.selectedSegmentIndex;
    [AppDelegate appDelegate].currentForm = selectedSegment;
    
    [self switchForm:selectedSegment];
}

-(void) switchForm:(int)formNumber {
    [AppDelegate appDelegate].currentForm = formNumber;
    
    UIView *view = [self.view viewWithTag:CURRENT_VIEW];
    [view removeFromSuperview];
    
    FormViewController *selectedView = [controllers objectAtIndex:formNumber];
    selectedView.view.tag = CURRENT_VIEW;
    [self.view addSubview:selectedView.view];
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    //self.firebase = [[Firebase alloc] initWithUrl:kFirebaseURL];
    
    FormViewController *form1VC = [[FormViewController alloc] initWithNibName:@"Form1" bundle:nil];
    form1VC.delegate = self;
    FormViewController *form2VC = [[FormViewController alloc] initWithNibName:@"Form2" bundle:nil];
    form2VC.delegate = self;
    FormViewController *form3VC = [[FormViewController alloc] initWithNibName:@"Form3" bundle:nil];
    form3VC.delegate = self;
    FormViewController *form4VC = [[FormViewController alloc] initWithNibName:@"Form4" bundle:nil];
    form4VC.delegate = self;
    FormViewController *form5VC = [[FormViewController alloc] initWithNibName:@"Form5" bundle:nil];
    form5VC.delegate = self;
    FormViewController *form6VC = [[FormViewController alloc] initWithNibName:@"Form6" bundle:nil];
    form6VC.delegate = self;
    FormViewController *form7VC = [[FormViewController alloc] initWithNibName:@"Form7" bundle:nil];
    form7VC.delegate = self;
    
    controllers = [[NSArray alloc] initWithObjects:form1VC, form2VC, form3VC, form4VC, form5VC, form6VC, form7VC, nil];
    FormViewController *fc = [controllers objectAtIndex:0]; // 1st view i.e default view
    fc.view.tag = CURRENT_VIEW;
    [AppDelegate appDelegate].currentForm = 0;
    [self.view addSubview:fc.view];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
