from the_bank import Account, Bank

if __name__ == "__main__":
	bank = Bank()
	newacc = Account('Charlie McG', 'bitebite')
	bank.add(newacc)
	if bank.transfer('Charlie McG', 'Charlie McG') is False:
		print("failed")
	else:
		print("success")
