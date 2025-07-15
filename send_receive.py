from lnbits_api import check_balance, pay_invoice, generate_invoice

def main():
    print("📲 Welcome to LNbits Terminal Wallet")
    
    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Send Sats")
        print("3. Receive Sats")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                balance = check_balance()
                print(f"💰 Your balance: {balance} sats")

            elif choice == "2":
                bolt11 = input("🔁 Paste BOLT11 Invoice: ").strip()
                result = pay_invoice(bolt11)
                print("✅ Payment sent:", result)

            elif choice == "3":
                amt = int(input("💸 Enter amount in sats to receive: "))
                invoice = generate_invoice(amt)
                print("📥 Share this invoice to receive payment:")
                print(invoice["payment_request"])

            elif choice == "4":
                print("👋 Goodbye.")
                break

            else:
                print("❌ Invalid choice. Try again.")

        except Exception as e:
            print("🚨 Error:", e)

if __name__ == "__main__":
    main()

