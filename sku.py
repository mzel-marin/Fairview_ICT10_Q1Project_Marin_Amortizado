from pyscript import display, document


def generate_sku(e):

    # Get Category
    category = document.getElementById("category").value

    # Get Product Name
    product_name = document.getElementById("product-name").value

    # Get Stock Quantity
    stock_qty = document.getElementById("stock-quantity").value


    # Check if fields are filled
    if category == "" or product_name == "" or stock_qty == "":
        document.getElementById("sku-result").innerHTML = "Please fill in all fields."
        return


    # Create the SKU
    sku = (
        category[:3].upper()
        + "-"
        + product_name[:4].upper()
        + "-"
        + str(stock_qty)
    )


    # Display the SKU
    document.getElementById("sku-result").innerHTML = "SKU: " + sku