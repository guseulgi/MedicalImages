import vtk


def main():
    colors = vtk.vtkNamedColors()
    bkg = map(lambda x: x / 255.0, [26, 51, 102, 255])
    colors.SetColor("BkgColor", *bkg)

    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(8)

    # Mapper 는 만들어준 모델을 커스텀할 수 있는 역할
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # Actor 는 Mapper와 Property를 모델에 적용시켜줌
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(colors.GetColor3d("White"))  # 색상 지정
    cylinderActor.RotateX(30.0)  # 회전
    cylinderActor.RotateY(-45.0)

    # Rnederer 는 Actor 를 렌더링 해주는 역할
    ren = vtk.vtkRenderer()

    # RenderWindow 는 렌더링 해줄 윈도우창 설정
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)

    # RenderWindowInteractor 는 카메라 등 설정
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Actor 를 Renderer 에 설정, RenderWindow 로 윈도우 설정
    ren.AddActor(cylinderActor)
    ren.SetBackground(colors.GetColor3d("BkgColor"))
    renWin.SetSize(300, 300)
    renWin.SetWindowName('CylinderExample')

    # RenderWindowInteractor 를 초기화
    iren.Initialize()

    # Renderer 카메라 설정 후 RenderWindow 로 렌더 처리
    ren.ResetCamera()
    ren.GetActiveCamera().Zoom(1.5)
    renWin.Render()

    # 설정해준 값들을 기반으로 RenderWindowInteractor의 이벤트 루프 시작
    iren.Start()


main()
