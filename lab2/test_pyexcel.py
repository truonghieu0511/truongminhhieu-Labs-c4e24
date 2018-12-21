import pyexcel
a_list_of_dic = [
    {
        "name" : "Hieu",
        "age " : 20
    },
    {
        "name" : "ha",
        "age " : 20
    }
]
pyexcel.save_as(records=a_list_of_dic, dest_file_name="a1.xlsx")