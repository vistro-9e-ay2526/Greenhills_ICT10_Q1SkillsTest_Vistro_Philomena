#Receipt Generator
from pyscript import document, display


def calculate_receipt(e):
    document.getElementById('output').innerHTML = " "   #clears previous outputs

    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    prod6 = document.getElementById("item6")
    prod7 = document.getElementById("item7")
    prod8 = document.getElementById("item8")

    #retrieves value of checked boxes
    price1 = float(prod1.value) * prod1.checked

    price2 = float(prod2.value) * prod2.checked
   
    price3 = float(prod3.value) * prod3.checked

    price4 = float(prod4.value) * prod4.checked
   
    price5 = float(prod5.value) * prod5.checked
   
    price6 = float(prod6.value) * prod6.checked
   
    price7 = float(prod7.value) * prod7.checked
   
    price8 = float(prod8.value) * prod8.checked
   

    subtotal = float(price1)+(price2)+(price3)+(price4)+(price5)+(price6)+(price7)+(price8)
    vat = 0.12 * subtotal
    rounded_vat = round(vat, 2)   #rounds off vat to 2 decimal places
    total = subtotal + vat

    display(f'Subtotal: {subtotal}', target="output") 
    display(f'VAT: {rounded_vat}', target="output")
    display(f'Total: {total}', target="output")
