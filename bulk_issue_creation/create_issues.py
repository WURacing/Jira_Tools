def get_multiselect_input(header, options):
    print(header)
    index = 1
    for o in options:
        print(str(index) + '. ' + o)
        index += 1
    selected_option = abs(int(input('>').strip()))
    if selected_option >= len(options):
        return options[0]
    return options[selected_option - 1]


def get_input(header):
    print(header)
    return input('>').strip()

emails = []

print('*' * 10 + ' JIRA bulk issue generator ' + '*' * 10)
print('This program will create a CSV which can be imported into JIRA to bulk create the same issue for multiple users.')
print('Aquiring users...')


with open('./users.txt', 'r') as userdata:
    for line in userdata.readlines():
        emails.append(line.strip())

print('Total of ' + str(len(emails)) + ' users detected')

ticket_type = get_multiselect_input('Ticket Type', ['Task', 'Defect'])
summary = get_input('Summary')
platform = get_multiselect_input('Platform', ['WUFR20', 'WUFR22', 'N/A'])
component = get_input('Component')
epic = get_multiselect_input('Ticket Type', ['Exec', 'Business', 'ABC', 'EDA', 'Suspension and Steering', 'Chassis', 'Drivetrain', 'Powertrain', 'Ergo', 'Manufacturing'])
release = get_input('Release')

with open('./output.csv', 'w+') as output:
    output.write('Ticket Type,Summary,Platform,Component,Epic,Release,User\n')
    for email in emails:
        output.write(','.join([ticket_type, summary, platform, component, epic, release, email]) + '\n')