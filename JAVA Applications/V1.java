  public static void main(String[] args) throws AWTException {
  try {
   Robot robot = new Robot();
   robot.mousePress(InputEvent.BUTTON1_MASK);
   robot.mouseRelease(InputEvent.BUTTON1_MASK);
   
  } catch (AWTException e) {
   e.printStackTrace();
  }
 }
