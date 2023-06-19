# file = open("student_records.txt", mode='w')
# file.write("001 mariam 75\n")
# file.write("002 david 75\n")
# file.write("003 sultan 75\n")
# file.write("004 torin 75\n")
# # file.close()
#
# with open("record2.txt", mode='w') as file:
#     file.write("005 hyelnati 75\n")
#     file.write("006, segun 75\n")
#     file.write("006, esther 75\n")
# with open ("product.text", mode='r') as file:
#     file .write("001 torin    40 \n")
#     file .write("002  always 400\n")
#     file .write("003 milk    700\n")
#     file .write("004 milo     1200\n")
#     file .write("005 egg     700\n")
#
# with open ("record2.txt", mode='r') as records:
#     for record in records:
#         num, name, score = record.split()
#         print(f"{name:<10} {score:>10}")
import json

#
# with open ("product.text", mode='r') as records:
#     for record in records:
#         num, name, score = record.split()
#         print(f"{num:<10}    {name:<10} {score:>10}")

# with open("product.text", mode='a') as records:
#     for record in records:
#         num, name, score = record.split()
#         print(f"{num:<10}    {name:<10} {score:>10}")
#
# file1 = open('record2.txt', mode='r')
# file2 = open('record.txt', 'w')
#
# with file1, file2:
#     for record in file1:
# #         sn, name, score = record.split()
# #         if sn != "008":
# #             file2.write(record)
# with open("record2.txt", mode='a') as file:
#     file.write("001 mikel 75\n")
#     file.write("002 emeka 75\n")
#     file.write("003 esther 75\n")
#     file.write("004 joseph 75\n")
#     file.write("005 ebuka 75\n")
#     file.write("007 dele 75\n")
#     file.write("008 bola 75\n")
#     file.write("009 zele 75\n")
#     file.write("010 fola 75\n")

# #
# file1 = open('record2.txt', mode='r')
# file2 = open('record.txt', mode='w')
#
# with file1, file2:
#     for record in file1:
#         sn, name, score = record.split()
#         if sn != "009":
#             file2.write(record)
#         else:
#             new_record = ' '.join([sn, "chukwuma", score])
#             file2.write(new_record + "\n")

records = {"studemt_records":[
    {"id": 1, "name": "ebuka", "age": 41},
    {"id": 2, "name": "emeka", "age": 30},
    {"id": 3, "name": "jessica", "age": 20},
    {"id": 4, "name": "moria", "age": 40},
]}

with open("records.json", mode='w') as rec:
    json.dump(records, rec)

with open("records.json", mode='r') as rec2:
    print(json.dumps(json.load(rec2), indent=4))


