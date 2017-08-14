
# open the file - and read all of the lines.
changes_file = 'changes_python.log'
# use strip to strip out spaces and trim the line.

#This function is used to find the day of the week which we know follows '(' and is followed by ',' in the date column.
def find_between( string, first, last ):
    try:
        start = string.index( first ) + len( first )
        end = string.index( last, start )
        return string[start:end]
    except ValueError:
        return ""

#Some comments included " as a quotation which was problematic because " was being used to denote which commas were not to be read as cell separators.
#This for loop replaces " with '
for line in changes_file:
	line.replace('"',"'")

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, day = None, hour = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.day = day
        self.hour = hour
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.day = find_between( details[2], '(', ',' )
        current_commit.hour = details[2][11:14]
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

print(len(commits))

commits.reverse()

for index, commit in enumerate(commits):
    print(commit.get_commit_comment())

	
output_file = 'changes.csv'
my_file = open(output_file, 'w')
my_file.write('Revision,Author,Date, Day, Hour, # Lines, Comment, Files Changed\n')
for commit in commits:
	my_file.write(str(commit.revision) + ',' +
			commit.author + ',"' +
			commit.date + '",' +
			commit.day + ',' +
			commit.hour + ',' +
			str(commit.comment_line_count) + ',"' +
			''.join(commit.comment) + '",' +
			' - '.join(commit.changes) + '\n')
my_file.close()






















