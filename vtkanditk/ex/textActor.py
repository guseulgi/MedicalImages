import vtk


def main():
    colors = vtk.vtkNamedColors()

    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.SetWindowName('TextActor')
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    txt = vtk.vtkTextActor()
    txt.SetInput('Hello World')
    txtprop = txt.GetTextProperty()
    txtprop.SetFontFamilyToArial()
    txtprop.BoldOn()
    txtprop.SetFontSize(40)
    txtprop.ShadowOn()
    txtprop.SetShadowOffset(4, 4)
    txtprop.SetColor(colors.GetColor3d('Cornsilk'))
    txt.SetDisplayPosition(20, 30)

    ren.AddActor(txt)
    ren.SetBackground(colors.GetColor3d('Black'))

    iren.Initialize()
    renWin.Render()
    iren.Start()


main()
