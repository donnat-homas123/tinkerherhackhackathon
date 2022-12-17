WebAutomation.LaunchChrome Url: 'https://blackknight.wd1.myworkdayjobs.com/BKC' BrowserInstance=> Browser
WAIT 5
MouseAndKeyboard.SendKeys TextToSend: $'''{End:5}''' DelayBetweenKeystrokes: 2000 SendTextAsHardwareKeys: False
WebAutomation.ExecuteJavascript BrowserInstance: Browser Javascript: $'''function ExecuteScript() {
 let nameList = [];
 let response = \'\';

 document.querySelectorAll(\'.gwt-Label.WJCP.WCBP\').forEach((element, i) => {
  nameList.push(element.innerHTML);

  let event = new MouseEvent(\'contextmenu\', {
   bubbles: true,
   cancelable: false,
   view: window,
   button: 2,
   buttons: 0,
   clientX: element.getBoundingClientRect().x,
   clientY: element.getBoundingClientRect().y
  });
  element.dispatchEvent(event);
 });

 document.querySelectorAll(\'div[data-automation-id=\"copyUrl\"]\').forEach((element, i) => {
  response += nameList[i] + \'\\\\t\' + element.getAttribute(\'data-clipboard-text\') + \'\\\\n\';
 });

 return response;
}''' Result=> Result
Text.SplitWithDelimiter Text: Result CustomDelimiter: $'''\\n''' IsRegEx: False Result=> TextList
Excel.Launch Visible: True LoadAddInsAndMacros: False Instance=> ExcelInstance
LOOP LoopIndex FROM 0 TO TextList.Count - 2 STEP 1
    Text.SplitWithDelimiter Text: TextList[LoopIndex] CustomDelimiter: $'''\\t''' IsRegEx: False Result=> TextList2
    Excel.WriteCell Instance: ExcelInstance Value: TextList2[0] Column: 1 Row: LoopIndex + 1
    Excel.WriteCell Instance: ExcelInstance Value: TextList2[1] Column: 2 Row: LoopIndex + 1
END
