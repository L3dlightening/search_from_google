def make_output_file_path(input_directory, output_directory, file_path):
    '''与えられたファイルのパスからファイル名だけを抜き取り、名前を変更して出力先のディレクトリへ出力する
    Args:
      input_directory: file_pathのファイル名までの入力パス
      output_directory: file_pathのファイル名までの出力パス
      file_path: 対象ファイルのパス
    '''
    file_name = file_path.replace(input_directory, '')
    file_name_without_csv = file_name.replace('.csv', '')
    output_path = output_directory + file_name_without_csv + '_output.csv'
    return output_path