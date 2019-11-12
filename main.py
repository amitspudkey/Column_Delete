import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def main():
    print("Program: Column Delete")
    print("Release: 0.1.2")
    print("Date: 2019-11-12")
    print("Author: Brian Neely")
    print()
    print()
    print("This program reads a csv file and deletes selected columns.")
    print()
    print()

    # Hide Tkinter GUI
    Tk().withdraw()

    # Find input file
    file_in = select_file_in()

    # Set output file
    file_out = select_file_out(file_in)

    # Ask for delimination
    delimination = input("Enter Deliminator: ")

    # Open input csv using the unknown encoder function
    data = open_unknown_csv(file_in, delimination)

    # Ask whether to use all columns, exclude certain columns, or select certain columns
    column_selection_type_input = column_selection_type(0)

    # Get list of columns for deletion
    columns = column_list(data, column_selection_type_input)

    # Delete Columns
    data_out = data.drop(columns, axis=1)

    # Write output file
    print("Writing output file...")
    data_out.to_csv(file_out, index=False)
    print("Output file wrote!")


def select_file_in():
    file_in = askopenfilename(initialdir="../", title="Select file",
                              filetypes=(("Comma Separated Values", "*.csv"), ("all files", "*.*")))
    if not file_in:
        input("Program Terminated. Press Enter to continue...")
        exit()

    return file_in


def select_file_out(file_in):
    file_out = asksaveasfilename(initialdir=file_in, title="Select file",
                                 filetypes=(("Comma Separated Values", "*.csv"), ("all files", "*.*")))
    if not file_out:
        input("Program Terminated. Press Enter to continue...")
        exit()

    # Create an empty output file
    open(file_out, 'a').close()

    return file_out


def y_n_question(question):
    while True:
        # Ask question
        answer = input(question)
        answer_cleaned = answer[0].lower()
        if answer_cleaned == 'y' or answer_cleaned == 'n':
            return answer_cleaned
        else:
            print("Invalid input, please try again.")


def column_list(data, column_selection_type_in):
    print("Reading Column List")
    headers = list(data.columns.values)
    if column_selection_type_in == 0:
        while True:
            try:
                print("Select which columns to keep...")
                for j, i in enumerate(headers):
                    print(str(j) + ": to keep column [" + str(i) + "]")

                # Ask for index list
                column_index_list_string = input("Enter selections separated by spaces: ")

                # Check if input was empty
                while not column_index_list_string:
                    column_index_list_string = input("Input was blank, please select columns to delete.")

                # Split string based on spaces
                column_index_list = column_index_list_string.split()

                # Get column names list
                column_name_list_excld = list()
                for i in column_index_list:
                    column_name_list_excld.append(headers[int(i)])

                column_name_list = list()
                for i in headers:
                    if i not in column_name_list_excld:
                        column_name_list.append(i)
            except:
                print("An invalid column input was detected, please try again.")
                continue

            else:
                break

    elif column_selection_type_in == 1:
        while True:
            try:
                print("Select columns to delete...")
                for j, i in enumerate(headers):
                    print(str(j) + ": to delete column [" + str(i) + "]")

                # Ask for index list
                column_index_list_string = input("Enter selections separated by spaces: ")

                # Check if input was empty
                while not column_index_list_string:
                    column_index_list_string = input("Input was blank, please select columns to delete.")

                # Split string based on spaces
                column_index_list = column_index_list_string.split()

                # Get column names list
                column_name_list = list()
                for i in column_index_list:
                    column_name_list.append(headers[int(i)])

            except:
                print("An invalid column input was detected, please try again.")
                continue

            else:
                break

    # Return column_name list to original function
    return column_name_list


def column_selection_type(start_index: int):
    # Ask whether to use all columns, exclude certain columns, or select certain columns
    selection_type = ["Enter 0 to delete all columns excluding selected columns.",
                      "Enter 1 to delete select columns."]

    while True:
        try:
            for index, i in enumerate(selection_type):
                if start_index <= index:
                    print(i)
            index_selection = int(input("Enter Selection: "))
            selection_type[index_selection]
            if index_selection < start_index:
                int("Error")
        except (ValueError, IndexError):
            print("Input must be integer between " + str(start_index) + " and " + str(len(selection_type) - 1))
            continue
        else:
            break
    return index_selection


def open_unknown_csv(file_in, delimination):
    encode_index = 0
    encoders = ['utf_8', 'latin1', 'utf_16',
                'ascii', 'big5', 'big5hkscs', 'cp037', 'cp424',
                'cp437', 'cp500', 'cp720', 'cp737', 'cp775',
                'cp850', 'cp852', 'cp855', 'cp856', 'cp857',
                'cp858', 'cp860', 'cp861', 'cp862', 'cp863',
                'cp864', 'cp865', 'cp866', 'cp869', 'cp874',
                'cp875', 'cp932', 'cp949', 'cp950', 'cp1006',
                'cp1026', 'cp1140', 'cp1250', 'cp1251', 'cp1252',
                'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257',
                'cp1258', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr',
                'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp',
                'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext',
                'iso2022_kr', 'latin_1', 'iso8859_2', 'iso8859_3', 'iso8859_4',
                'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9',
                'iso8859_10', 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15',
                'iso8859_16', 'johab', 'koi8_r', 'koi8_u', 'mac_cyrillic',
                'mac_greek', 'mac_iceland', 'mac_latin2', 'mac_roman', 'mac_turkish',
                'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32',
                'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le',
                'utf_7', 'utf_8', 'utf_8_sig']

    data = open_file(file_in, encoders[encode_index], delimination)
    while data is str:
        if encode_index < len(encoders) - 1:
            encode_index = encode_index + 1
            data = open_file(file_in, encoders[encode_index], delimination)
        else:
            print("Can't find appropriate encoder")
            exit()

    return data


def open_file(file_in, encoder, delimination):
    try:
        data = pd.read_csv(file_in, low_memory=False, encoding=encoder, delimiter=delimination)
        print("Opened file using encoder: " + encoder)

    except UnicodeDecodeError:
        print("Encoder Error for: " + encoder)
        return "Encode Error"
    return data


if __name__ == '__main__':
    main()
