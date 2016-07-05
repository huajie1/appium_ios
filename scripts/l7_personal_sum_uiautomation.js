
var target = UIATarget.localTarget();
var window = target.frontMostApp().mainWindow();
var app = target.frontMostApp()

target.setDeviceOrientation(UIA_DEVICE_ORIENTATION_PORTRAIT);
window.textFields()["IntegerA"].tap();
app.keyboard().typeString("5");
window.textFields()["TextField2"].tap();
app.keyboard().typeString("6");
app.keyboard().typeString("\n");
window.buttons()["ComputeSumButton"].tap();
answer = window.staticTexts()["Answer"].value();

if (answer == 11){
    UIALogger.logPass("Passed");
}
else{
    UIALogger.logFail("The result is "+answer)
}
