import csv 
ok = 0
print("Welcome!")
def register_event():
    try:
        event_name = input("Write the name of the event: ")
        date = input("Write the date of the event: ")
    except NameError:
        print("This event is not defined")
    except:
        print("Something else went wrong. Try again! ")
    finally:
        write.writerow([event_name, date])
        print('Thank you')
    
if ok == 1:
    #create an csv file
    with open('events.csv', 'w', newline='') as f:
        fieldnames = ['event_name', 'date']
        csv_file = csv.reader(open('events.csv', "r"), delimiter=",")
        write = csv.writer(f, quoting=csv.QUOTE_ALL) 
        register_event()
        ok = 0
        #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
else:
    print("Choose the number you need\n 1. Create an event\n2. See the existing events\n3. Delete an event" )
    num = input()
    if num == 1:
        with open('events.csv', 'a', newline='') as f:
            fieldnames = ['event_name', 'date']
            write = csv.writer(f, quoting=csv.QUOTE_ALL) 
            register_event()
    else:
        if num ==2:
            with open('events.csv', 'r', newline='') as f:
                fieldnames = ['event_name', 'date']
                csv_file = csv.reader(open('events.csv', "r"), delimiter=",")
                write = csv.writer(f, quoting=csv.QUOTE_ALL) 
                print("Our events:\n", write)
        else:
            print("Type the name of the event: ")
            del_event = input()
            with open('events.csv', 'r', newline='') as f:
                csv_file = csv.reader(open('events.csv', "r"), delimiter=",")
                for raw in  csv_file:
                    if del_event == row[1]:
                        event_name.remove(del_event)
                        print(del_event, ' is cancelled!')







