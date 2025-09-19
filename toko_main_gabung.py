from tabulate import tabulate
import random


db_operator_data = { 1101: ["Axel", "abc123"],
                1102: ["Lukman", "bcd234"],
                1103 : ["Almira", "cde345"],
                1104 : ["Hashfi", "def456"],
                1105 : ["Zulfan", "efg567"],
                1106 : ["Krysna", "fgh678"],
                1107 : ["Bayu", "ghi789"]
}

db_classifications = ["kategori", "barang", "brand"]
db_aksi_user = ["dilihat","dihapus", "ditambah"]

db_shop_items = {
    "food": {
        "milk": {
            "nestle": {"price": 10000, "stock": 20, "ID": 101},
            "oatside": {"price": 12000, "stock": 15, "ID": 102}
        },
        "bread": {
            "BrandA": {"price": 14000, "stock": 35, "ID": 103},
            "BrandB": {"price": 13000, "stock": 25, "ID": 104}
        }
    },
    "drinks": {
        "juice": {
            "abc": {"price": 20000, "stock": 30, "ID": 105},
            "sunkist": {"price": 22000, "stock": 20, "ID": 106}
        }
    },
    "work supplies": {
        "notebook": {
            "kiki": {"price": 35000, "stock": 50,"ID": 107},
            "estudee": {"price": 40000, "stock": 40, "ID": 108}
        },
        "pen": {
            "pilot": {"price": 8000, "stock": 100, "ID": 109},
            "snowman": {"price": 10000, "stock": 80, "ID": 110}
        }
    }
}
db_discount = [0.2, 0.15, 0.15, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05]
db_member = {"pimpi" : 1, "fikri" : 2, "badu": 3}

#===========================================================================================================================
def f_input_checker(inputs):
    try:
        inputs = int(inputs)
        return inputs
    except ValueError:
        return None


def f_login():
    tries_left = 5
    masuk = False
    while not masuk:
        operator_id = (input("Silakan masukkan id anda: "))
        operator_id = f_input_checker(operator_id)

        if operator_id in db_operator_data:
            print(f"Selamat datang {db_operator_data[operator_id][0]}") #print nama sesuai id

            password = False
            while not password:
                if tries_left == 0:
                    print("Mohon maaf, Anda telah melebihi batas percobaan sebesar 5 kali")
                    return False
                operator_password = input("Silakan masukkan password: ") #case sensitive
                if operator_password == db_operator_data[operator_id][1]:
                    print("Access Granted!")
                    return True
                else:
                    print("Wrong password, try again!")
                    tries_left -= 1
                    coba_again_pass = False
                    while not coba_again_pass:
                        coba_lagi_pass = input("Apakah anda ingin mencoba lagi (y/n): ").lower()
                        if coba_lagi_pass == "y":
                            coba_again_pass = True
                        elif coba_lagi_pass == "n":
                            password = True
                            coba_again_pass = True
                        else:
                            print("Silakan pilih antara (y/n)")

        else:
            print("Mohon maaf, ID Anda tidak terdata")
            coba_again = False
            while not coba_again:
                coba_lagi = input("Apakah anda ingin mencoba lagi (y/n): ").lower()
                if coba_lagi == "y":
                    coba_again = True
                elif coba_lagi == "n":
                    return False

                else:
                    print("Silakan pilih antara (y/n)")


def f_show_shop_items(data, category_filter = None, product_filter = None, brand_filter = None):
    table = []
    index = 1

    for category, products in data.items():
        if category_filter and category != category_filter:
            continue  # tidak memasukkan category_filter pada table
        for product, brands in products.items():
            if product_filter and product != product_filter:
                continue
            for brand, details in brands.items():
                if brand_filter and brand != brand_filter:
                    continue
                row = [index, category, product, brand, details["price"], details["stock"], details["ID"]]
                table.append(row)
                index += 1

    headers = ["Index", "Category", "Item", "Brand", "Price", "Stock", "ID"]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


def f_shop_items_filtered(index_classification):
    index_classification = f_input_checker(index_classification)
    if index_classification is None:
        print("Mohon maaf opsi tidak tersedia")
        return

    list_filtered = []
    if index_classification == 0:
        for categories, products in db_shop_items.items():
            list_filtered.append(categories)
    elif index_classification == 1:
        for categories, products in db_shop_items.items():
            for product in products.keys():
                list_filtered.append(product)
    elif index_classification == 2:
        for categories, products in db_shop_items.items():
            for product, brands in products.items():
                for brand, details in brands.items():
                    if brand not in list_filtered: #filter biar tidak ada data yang double
                        list_filtered.append(brand)
    return list_filtered


def f_show_user_category_option(index_classification, user_action):
    list_filtered = f_shop_items_filtered(index_classification)

    print(f"List {db_classifications[index_classification]} :")
    for objects in list_filtered:
        print(f"{list_filtered.index(objects) + 1}. {objects}")
    angka_filtered = input(f"Pilih angka {db_classifications[index_classification]} yang akan {db_aksi_user[user_action]}: ")
    angka_filtered = f_input_checker(angka_filtered)
    if angka_filtered is None or angka_filtered <= 0 or angka_filtered > len(list_filtered):
        print(f"Mohon maaf, {db_classifications[index_classification]} tersebut tidak tersedia")
        return None
    else:
        return angka_filtered


def f_show_shop_items_filtered(index_classification, user_action):
    angka_filtered = f_show_user_category_option(index_classification, user_action)
    if angka_filtered is None or angka_filtered <= 0: #jika opsi tidak ada maka langsung keluar function
        return None
    else:
        list_filtered = f_shop_items_filtered(index_classification)
        filter_dipilih = list_filtered[angka_filtered - 1]
        if index_classification == 0:
            f_show_shop_items(db_shop_items, category_filter=filter_dipilih)
            return angka_filtered
        elif index_classification == 1:
            f_show_shop_items(db_shop_items, category_filter = None, product_filter = filter_dipilih)
            return angka_filtered
        elif index_classification == 2:
            f_show_shop_items(db_shop_items, category_filter= None, product_filter= None, brand_filter = filter_dipilih)
            return angka_filtered


def f_id_adder():
    max_id = 100  #base sebagai acuan
    for categories, products in db_shop_items.items():
        for product, items in products.items():
            for brand, details in items.items():
                max_id = max(max_id, details["ID"]) #akan mencari nilai max di database
    return max_id + 1


def f_show_cart(data, category_filter = None, product_filter = None, brand_filter = None):
    table = []
    index = 1

    for category, products in data.items():
        if category_filter and category != category_filter:
            continue  # tidak memasukkan category_filter pada table
        for product, brands in products.items():
            if product_filter and product != product_filter:
                continue
            for brand, details in brands.items():
                if brand_filter and brand != brand_filter:
                    continue
                details["total price"] = details["quantity"] * details["price"]
                row = [index, details["ID"], product, brand, details["quantity"], details["price"], details["total price"] ]
                table.append(row)
                index += 1

    headers = ["Index", "ID", "Item", "Brand", "Quantity",  "Price", "Total Price"  ]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


def f_add_to_cart(cart, categories, product, brand, details, qty_cart):
    if categories not in cart: # Menambahkan kategori jika belom ada
        cart[categories] = {}
    if product not in cart[categories]:# Menambahkan barang jika belom ada
        cart[categories][product] = {}
    if brand not in cart[categories][product]: # Menambahkan brand jika belom ada
        cart[categories][product][brand] = {
            'price': details['price'],
            'quantity': qty_cart,
            'ID': details['ID']
        }
    else:
        cart[categories][product][brand]['quantity'] += qty_cart # Jika barang sudah ada, hanya update quantity saja
    details['stock'] -= qty_cart # Mengurangi stok

# ==========================================================================================================================
uang_masuk = 0
while True:
    user = input("=== MENU USER ===\n1. operator\n2. customer\n3. Keluar\nPilihan: ")
    user = f_input_checker(user)

    if user == 1:
        operator = f_login()
        while operator:
            opsi_operator = input("""
    === MENU UTAMA ===
    1. List barang
    2. Update barang
    3. Cek uang masuk
    4. Lihar daftar member
    5. Keluar
    Option: """)
            opsi_operator = f_input_checker(opsi_operator)

            if opsi_operator == 1:
                while True:
                    print("""
    === MENU LIST BARANG ===
    1. Semua Barang
    2. Berdasarkan Kategori
    3. Berdasarkan barang
    4. Berdasarkan brand
    5. Keluar""")
                    read_operator = input("Pilih opsi penglihatan barang: ")
                    read_operator = f_input_checker(read_operator)
                    if read_operator == 1:
                        f_show_shop_items(db_shop_items)
                    elif read_operator == 2:
                        f_show_shop_items_filtered(0,0)
                    elif read_operator == 3:
                        f_show_shop_items_filtered(1,0)
                    elif read_operator == 4:
                        f_show_shop_items_filtered(2,0)
                    elif read_operator == 5:
                        print("Kembali ke menu")
                        break
                    else:
                        print("Mohon maaf opsi tidak tersedia")
                        continue

            elif opsi_operator == 2:
                while True:
                    f_show_shop_items(db_shop_items)
                    print("""
    === MENU UPDATE BARANG ===
    1. Menambahkan
    2. Menghapus
    3. Update
    4. Keluar""")
                    action_operator = input("Pilih opsi update barang: ")
                    action_operator = f_input_checker(action_operator)
                    if action_operator == 1:
                        print("""
    === OPSI PENAMBAHAN ===
    1. Kategori
    2. Barang
    """)
                        penambahan_operator = input("Pilih opsi penambahan: ")
                        penambahan_operator = f_input_checker(penambahan_operator)
                        if penambahan_operator == 1:
                            tambah_kategori = input("Masukkan kategori baru: ").lower()
                            if tambah_kategori in db_shop_items:
                                print("kategori sudah ada")
                            else:
                                db_shop_items[tambah_kategori] = {}
                                print("Kategori berhasil ditambahkan!")

                        elif penambahan_operator == 2:
                            angka_filtered = f_show_user_category_option(0, 2)
                            if angka_filtered is not None:
                                list_kategori = list(db_shop_items.keys())
                                kategori_barang = list_kategori[angka_filtered-1]
                                barang_baru = input("Input barang baru: ").lower()
                                brand_baru = input("Input brand barang: ")
                                if barang_baru in db_shop_items[kategori_barang] and brand_baru in db_shop_items[kategori_barang][barang_baru]:
                                    print(f"Mohon maaf,{barang_baru} dengan brand {brand_baru} sudah tersedia.")
                                else:
                                    price_baru = input("Input harga barang: ")
                                    stock_baru = input("input stock barang: ")
                                    price_baru = f_input_checker(price_baru)
                                    stock_baru = f_input_checker(stock_baru)
                                    if price_baru is not None and stock_baru is not None and price_baru >0 and stock_baru > 0:
                                        if barang_baru not in db_shop_items[kategori_barang]:
                                            db_shop_items[kategori_barang][barang_baru] = {}
                                        db_shop_items[kategori_barang][barang_baru][brand_baru] = {
                                                                                                    "price": price_baru,
                                                                                                    "stock": stock_baru,
                                                                                                    "ID" : f_id_adder()
                                                                                                        }
                                    else:
                                        print("Masukkan harga dan stock yang benar")
                        else:
                            print("Mohon maaf opsi tidak tersedia")

                    elif action_operator == 2:
                        print("""
    === OPSI PENGHAPUSAN ===                        
    1. Kategori
    2. Barang""")
                        pengurangan_operator = input("Pilih opsi penghapusan: ")
                        pengurangan_operator = f_input_checker(pengurangan_operator)
                        if pengurangan_operator == 1:
                            delete_kategori =  f_show_user_category_option(0, 1)
                            while True and delete_kategori:
                                make_sure = input("Apakah anda yakin ingin melakukan penghapusan (y/n): ").lower()
                                if make_sure == "y":
                                    list_kategori = f_shop_items_filtered(0)
                                    kategori_barang = list_kategori[delete_kategori - 1]
                                    del db_shop_items[kategori_barang]
                                    print("Kategori berhasil dihapus")
                                    break
                                elif make_sure == "n":
                                    print("Kembali ke menu")
                                    break
                                else:
                                    print("Silakan pilih antara (y/n)")


                        elif pengurangan_operator == 2:
                            print("""
    ==OPSI PENGHAPUSAN BERDASARKAN ==
    1. Nama Barang
    2. ID Barang""")
                            pengurangan_operator_barang = input("Pilihan: ")
                            pengurangan_operator_barang = f_input_checker(pengurangan_operator_barang)
                            if pengurangan_operator_barang == 1:
                                delete_barang = f_show_user_category_option(1, 1)
                                while True and delete_barang:
                                    make_sure = input("Apakah anda yakin ingin melakukan penghapusan (y/n): ").lower()
                                    if make_sure == "y":
                                        list_barang = f_shop_items_filtered(1)
                                        barang_dihapus = list_barang[delete_barang - 1]
                                        for categories, products in db_shop_items.items():
                                            if barang_dihapus in products: #mencari barang yang ingin dihapus
                                                del db_shop_items[categories][barang_dihapus] #menghapus barang
                                                break
                                    elif make_sure == "n":
                                        print("Kembali ke menu")
                                        break
                                    else:
                                        print("Silakan pilih antara (y/n)")
                                    break

                            elif pengurangan_operator_barang == 2:
                                id_barang_dihapus = input("Masukkan ID barang yang ingin dihapus: ")
                                id_barang_dihapus = f_input_checker(id_barang_dihapus)

                                found = False
                                for categories, products in db_shop_items.items():
                                    for product, brands in products.items():
                                        for brand, details in brands.items():
                                            if details["ID"] == id_barang_dihapus:
                                                found = True
                                                delete = False
                                                while not delete:
                                                    make_sure = input("Apakah anda yakin ingin melakukan penghapusan (y/n): ").lower()
                                                    if make_sure == "y":
                                                        del db_shop_items[categories][product][brand] #menghapus dictionary dengan value id tersebut
                                                        print(f"Barang dengan ID : {id_barang_dihapus} berhasil dihapus")
                                                        delete = True
                                                    elif make_sure == "n":
                                                        print("Kembali ke menu")
                                                        break
                                                    else:
                                                        print("Silakan pilih antara (y/n)")
                                            if found:
                                                break
                                        if found:
                                            break
                                if not found:
                                    print("ID barang tidak ada")

                            else:
                                print("Mohon maaf opsi tersebut tidak tersedia")
                        else:
                            print("Mohon maaf opsi tersebut tidak tersedia")

                    elif action_operator == 3: #hanya bisa update price dan stock
                        found = False
                        id_barang_diedit = input("Masukkan ID barang yang ingin diedit: ")
                        id_barang_diedit = f_input_checker(id_barang_diedit)
                        for categories, products in db_shop_items.items():
                            for product, brands in products.items():
                                for brand, details in brands.items():
                                    if details["ID"] == id_barang_diedit:
                                        found = True
                                        update = False
                                        price_baru = input("Masukkan harga baru: ")
                                        price_baru = f_input_checker(price_baru)
                                        stock_baru = input("Masukkan stock baru: ")
                                        stock_baru = f_input_checker(stock_baru)
                                        if price_baru is None or stock_baru is None:
                                            print("Mohon masukkan harga dan stock yang benar")
                                            break
                                        while not update:
                                            make_sure = input("Apakah anda yakin ingin melakukan update (y/n): ").lower()
                                            if make_sure == "y":
                                                details["price"] = price_baru
                                                details["stock"] = stock_baru
                                                update = True
                                                print("Barang berhasil diupdate!")
                                            elif make_sure == "n":
                                                print("Kembali ke menu")
                                                break
                                            else:
                                                print("Silakan pilih antara (y/n)")
                                        break
                                if found:
                                    break
                            if found:
                                break
                        if not found:
                            print("ID barang tersebut tidak tersedia")

                    elif action_operator == 4:
                        break

                    else:
                        print("Mohon maaf opsi tidak tersedia")

            elif opsi_operator == 3:
                print(f"Total uang masuk ialah: {uang_masuk}")

            elif opsi_operator == 4:
                table_member = tabulate(db_member.items(), headers=["Nama", "ID"], tablefmt = "fancy_grid")
                print(table_member)

            elif opsi_operator == 5:
                print("Kembali ke menu")
                operator = False

            else:
                print("Mohon maaf opsi tidak tersedia")

    elif user == 2:
        cart = {}
        customer = True
        while customer:
            opsi_customer = input("""
    === MENU UTAMA ===
    1. Lihat Keranjang
    2. Tambah Barang 
    3. Kurangi Barang
    4. Checkout
    5. Keluar
    Option: """)
            opsi_customer = f_input_checker(opsi_customer)

            if opsi_customer == 1:
                f_show_cart(cart)

            elif opsi_customer == 2:
                tambah_produk = True
                while tambah_produk:
                    print("""
    === OPSI PENGLIHATAN BARANG ===
    1. Semua Barang
    2. Berdasarkan Kategori
    3. Berdasarkan barang
    4. Berdasarkan brand
    5. Keluar""")

                    read_customer = input("Pilih opsi penglihatan barang: ")
                    read_customer = f_input_checker(read_customer)
                    if read_customer == 1:
                        f_show_shop_items(db_shop_items)
                        pesan = 1
                    elif read_customer == 2:
                        pesan = f_show_shop_items_filtered(0, 0)
                    elif read_customer == 3:
                        pesan = f_show_shop_items_filtered(1, 0)
                    elif read_customer == 4:
                        pesan = f_show_shop_items_filtered(2, 0)
                    elif read_customer == 5:
                        print("Kembali ke menu")
                        break
                    else:
                        print("Mohon maaf opsi tidak tersedia")
                        break

                    if pesan is not None:
                        add_cart = False
                        while not add_cart:
                            customer_input = input("apakah sudah siap untuk memesan? (y/n): ").lower()
                            if customer_input == 'y':
                                    id_barang_cart = input("Masukkan ID barang yang ingin ditambah ke keranjang: ")
                                    id_barang_cart = f_input_checker(id_barang_cart)
                                    if id_barang_cart is None:
                                        print("Mohon maaf ID tersebut tidak tersedia")
                                        break

                                    found = False
                                    for categories, products in db_shop_items.items():
                                        for product, brands in products.items():
                                            for brand, details in brands.items():
                                                if details["ID"] == id_barang_cart:
                                                    found = True
                                                    qty_cart = input("Masukkan quantity yang anda mau: ")
                                                    qty_cart = f_input_checker(qty_cart)
                                                    if qty_cart is not None:
                                                        if qty_cart > details["stock"]:
                                                            print("Mohon maaf, stock tidak tersedia")
                                                            continue
                                                        else:
                                                            f_add_to_cart(cart, categories, product, brand, details, qty_cart)
                                                            continue_shopping = input("apakah anda masih mau melanjutkan pemilihan barang (y/n): ").lower()
                                                            if continue_shopping == 'y':
                                                                pesan_barang = False
                                                                add_cart = True
                                                            elif continue_shopping == 'n':
                                                                pesan_barang = False
                                                                tambah_produk = False
                                                                add_cart = True
                                                            else:
                                                                print("Silakan pilih antara (y/n)")
                                                if found:
                                                    break
                                            if found:
                                                break
                                        if found:
                                            break
                                    if not found:
                                        print("ID barang tidak ada")


                            elif customer_input == 'n':
                                add_cart = True
                                continue
                            else:
                                print("Silakan pilih antara (y/n): ")


            elif opsi_customer == 3:
                f_show_cart(cart)
                make_sure = input("Apakah anda yakin ingin menghapus barang? (y/n): ").lower()
                if make_sure == "y":
                    customer_input = input("Plilih ID barang yang akan dihapus: ")
                    customer_input = f_input_checker(customer_input)
                    if customer_input is None:
                        print("Masukkan ID berupa angka")
                        continue
                    found = False
                    for categories, products in cart.items():
                        for product, brands in products.items():
                            for brand, details in brands.items():
                                if details["ID"] == customer_input:
                                    found = True
                                    qty_hapus = input("Masukkan quantity barang yang akan dihapus: ")
                                    qty_hapus = f_input_checker(qty_hapus)
                                    if qty_hapus is None:
                                        print("Masukkan quantity yang benar")
                                        break
                                    if qty_hapus > details["quantity"]:
                                        print("Mohon maaf, quantity di keranjang Anda tidak mencukupi")
                                        break
                                    elif qty_hapus == details["quantity"]:
                                        db_shop_items[categories][product][brand]["stock"] += qty_hapus
                                        del cart[categories][product][brand]
                                        break
                                    elif qty_hapus < details["quantity"]:
                                        details['quantity'] -= qty_hapus
                                        db_shop_items[categories][product][brand]["stock"] += qty_hapus
                                        break
                                if found:
                                    break
                            if found:
                                break
                        if found:
                            break
                    if not found:
                        print("ID barang tidak ada")

                elif make_sure == "n":
                    print("Kembali ke menu")
                else:
                    print("Mohon maaf opsi tersebut tidak tersedia")

            elif opsi_customer == 4:
                check_out = True
                while check_out:
                    f_show_cart(cart)
                    make_sure = input("Apakah anda yakin ingin checkout? (y/n): ").lower()

                    if make_sure == "y":
                        sum_total = 0
                        for categories, products in cart.items():
                            for product, brands in products.items():
                                for brand, details in brands.items():
                                    sum_total += details["total price"]

                        print(f"Totalnya ialah {sum_total} rupiah")

                        diskon_option = input( "Apakah anda ingin daftar sebagai member untuk mendapatkan diskon (y/n): ").lower()
                        if diskon_option == "y":
                            discount = False
                            while not discount:
                                cust_member = input("Masukkan nama anda: ").lower()
                                id_member = input("Masukkan id anda: ")
                                id_member = f_input_checker(id_member)
                                if id_member is None:
                                    print("Kolom id hanya berbentuk angka")
                                    continue
                                if cust_member in db_member:
                                    if id_member == db_member[cust_member]:
                                        print("Anda sudah merupakan member")
                                        discount = True
                                else:
                                    db_member[cust_member] = id_member
                                    diskon = random.choice(db_discount)
                                    print(f"Anda mendapat diskon sebesar {diskon * 100}%")
                                    sum_total = sum_total * (1 - diskon)
                                    discount = True
                        elif diskon_option == "n":
                            print("Anda memilih untuk tidak daftar member")
                        else:
                            print("bukan opsi bro")
                            continue

                        paying = True
                        while paying:
                            print(f"Totalnya ialah {sum_total} rupiah")
                            pay = input("Apakah Anda jadi checkout (y/n):" ).lower()
                            if pay == "y":
                                jumlah_uang = float(input("Masukkan Jumlah Uang: "))
                                selisih = jumlah_uang - sum_total
                                if selisih < 0:  # jika uang kurang
                                    print(f"Uang anda kurang sebesar {round(abs(selisih), 2)}")
                                    continue
                                else:
                                    uang_masuk += sum_total #menambahkan ke total keuntungan yang diperoleh toko
                                    print("Terima kasih")
                                    if selisih > 0:  # jika ada kembalian
                                        print(f"Uang kembalian anda : {selisih}")
                                    paying = False
                                    customer = False
                                    check_out = False
                                break
                            elif pay == "n":
                                print("Kembali ke display keranjang!")
                                paying = False
                            else:
                                print("Mapp bro opsi ga tersedia")

                    elif make_sure == "n":
                        print("Kembali ke menu")
                        break
                    else:
                        print("Mohon maaf opsi tidak tersedia")

            elif opsi_customer == 5:
                exit_cust = False
                while not exit_cust:
                    make_sure = input("Apakah anda yakin mau keluar, semua item di keranjang akan hilang (y/n): ")
                    if make_sure == "y":
                        print("Baik terima kasih!")
                        customer = False
                        exit_cust = True
                    elif make_sure == "n":
                        print("Kembali ke menu")
                        exit_cust = True
                    else:
                        print("Silakan ketik (y/n)")

            else:
                print("Mohon maaf opsi tidak tersedia!")

    elif user == 3:
        print("Terima Kasih!")
        break

    else:
        print("Mohon maaf opsi tidak tersedia")
