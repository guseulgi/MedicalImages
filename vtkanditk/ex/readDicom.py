import vtk


def get_program_parameters():
    import argparse
    description = 'Read Dicom image data'
    epilogue = ''''''
    parser = argparse.ArgumentParser(
        description=description, epilog=epilogue, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='prostate.img')
    args = parser.parse_args()
    return args.filename


def main():
    colors = vtk.vtkNamedColors()
    input_filename = get_program_parameters()  # 명령어 실행 시 파일 경로를 읽어오는 함수

    # Read the DICOM file
    reader = vtk.vtkDICOMImageReader()
    reader.SetFileName(input_filename)
    reader.Update()

    # Visualize
    image_viewer = vtk.vtkImageViewer2()
    image_viewer.SetInputConnection(reader.GetOutputPort())

    render_window_interactor = vtk.vtkRenderWindowInteractor()
    image_viewer.SetupInteractor(render_window_interactor)
    image_viewer.Render()

    image_viewer.GetRenderer().SetBackground(colors.GetColor3d("SlateGray"))
    image_viewer.GetRenderWindow().SetWindowName("ReadDICOM")
    image_viewer.GetRenderer().ResetCamera()
    image_viewer.Render()

    render_window_interactor.Start()


main()
