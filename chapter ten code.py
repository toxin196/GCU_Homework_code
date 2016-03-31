
def make_data_set(file_name): # file name i s a s t r ing
    """Read f i l e file name ( s t r ) ; return l i s t of tupl e s in format :
    id , diagnosis , 9 at t r ibut e s . """
    input_set_list = []

# open f i l e . Fix the e r ror checking
    input_file = open(file_name)

    for line_str in input_file:
        line_str = line_str.strip() # s t r i p o f f end−of−l ine character " \n"
        # i f a ' ? ' in the patient data , skip that patient
        if '?' in line_str:
            continue
        id_str,a1,a2,a3,a4,a5,a6,a7,a8,a9,diagnosis_str = line_str.split(',')
        if diagnosis_str == '4': # diagnosis i s "malignant"
            diagnosis_str = 'm'
        else:
            diagnosis_str = 'b' # diagnosis i s "benign"
        patient_tuple=id_str,diagnosis_str,int(a1),int(a2),int(a3),int(a4),\
            int(a5),int(a6),int(a7),int(a8),int(a9)
        input_set_list.append(patient_tuple)
    return input_set_list


def sum_lists(list1,list2):
    """ Element−by−element sums of two l i s t s of 9 items . """
    sums_list = []
    for index in range(9):
        sums_list.append(list1[index]+list2[index])
    return sums_list

def make_averages(sums_list,total_int):
    """Convert each l i s t element into an average by dividing by the t o tal . """
    averages_list = []
    for value_int in sums_list:
        averages_list.append(value_int/total_int)
    return averages_list

def train_classifier(training_set_list):
    """Build a c l a s s i f i e r using the training s e t . """
    benign_sums_list=[0]*9 # l i s t of sums of benign a t t r i b u t e s
    benign_count=0 # count of benign patients
    malignant_sums_list=[0]*9 # l i s t of sums of malignant a t t r i b u t e s
    malignant_count=0 # count of malignant patients

    for patient_tuple in training_set_list:
        if patient_tuple[1]=='b': # i f benign diagnos i s
            # add benign a t t r i b u t e s to benign t o t a l
            benign_sums_list=sum_lists(benign_sums_list,patient_tuple[2:])
            benign_count += 1
        else: # e l s e malignant diagnos i s
            # add malignant a t t r ibut e s to malignant t o t a l
            malignant_sums_list=sum_lists(malignant_sums_list,patient_tuple[2:])
            malignant_count += 1

    # find averages of each s e t of benign or malignant a t t r i b u t e s
    benign_averages_list=make_averages(benign_sums_list,benign_count)
    malignant_averages_list=make_averages(malignant_sums_list,malignant_count)

    # separator values for each attribute averages benign and malignant
    classifier_list=make_averages(sum_lists(benign_averages_list,
                                            malignant_averages_list),2)

    return classifier_list

def classify_test_set(test_set_list, classifier_list):
    """ Given t e s t s e t and c l a s s i f i e r , c l a s s i s f y each patient in t e s t s e t ;
    return l i s t of r e sul t tupl e s : ( id , benign count , malignant count ,diagnosis )"""
    result_list = []
    # for each patient
    for patient_tuple in test_set_list:
        benign_count = 0
        malignant_count = 0
        id_str, diagnosis_str = patient_tuple[:2]
        # for each at t r ibut e of the patient ,
        for index in range(9):
            # i f actual patient at t r ibut e i s gr eat e r than s eparator value
            # "+2" s k i p s id and diagnos i s in l i s t
            if patient_tuple[index+2] > classifier_list[index]:
                malignant_count += 1
            else:

                benign_count += 1
            result_tuple = (id_str,benign_count,malignant_count,diagnosis_str)
            result_list.append(result_tuple)
    return result_list

def report_results(result_list):
    ' ' 'Check r e sul t s and report count of inaccurate c l a s s i f i c a t i o n s . ' ' '
    total_count=0
    inaccurate_count = 0
    for result_tuple in result_list:
        benign_count, malignant_count, diagnosis_str = result_tuple[1:4]
        total_count += 1
        if (benign_count > malignant_count) and (diagnosis_str == 'm'):
            # oops ! wrong c l a s s i f i c a t i o n
            inaccurate_count += 1
        elif diagnosis_str == 'b': # and ( benign count < malignant count )
            # oops ! wrong c l a s s i f i c a t i o n
            inaccurate_count += 1
            print("Of ",total_count," patients, there were ",\
            inaccurate_count," inaccuracies")

def main():

    print("Reading in training data...")
    training_file = "training data.txt"
    training_set_list = make_data_set(training_file)
    print("Done reading training data.\n")

    print("Training classifier...")
    classifier_list = train_classifier(training_set_list)
    print("Done training classifier.\n")

    print("Reading in test data...")
    test_file = "test data.txt"
    test_set_list = make_data_set(test_file)
    print("Done reading test data.\n")

    print("Classifying records...")
    result_list = classify_test_set(test_set_list, classifier_list)
    print("Done classifying.\n")

    report_results(result_list)

    print("Program finished.")
