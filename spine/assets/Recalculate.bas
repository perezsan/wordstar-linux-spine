REM  *****  BASIC  *****

Sub Recalculate()
   'ThisComponent.calculateAll()  ' Not needed
   ThisComponent.store()
   ThisComponent.close(True)
   dispatcher = createUnoService("com.sun.star.frame.DispatchHelper")
   dispatcher.executeDispatch(StarDesktop, ".uno:Quit", "", 0, Array())
End Sub
