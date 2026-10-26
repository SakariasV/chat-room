import pickle


# Where the code for the client goes


userdata = {'username' : 'zaki', 'pasword' : '123'}


pickle.dump(userdata,open('userdata.pkl', 'wb'))
loaded = pickle.load(open('userdata.pkl', 'rb'))

print(loaded)