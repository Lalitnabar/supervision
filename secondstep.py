from taipy import Gui
import webbrowser

# Main page content with clickable links
main_page = """
# Proactive Supervision

Proactive supervision is a forward-looking approach aimed at strengthening the regulatory compliance and risk management frameworks of cooperative banks and regional rural banks (RRBs). This strategy involves regular, constructive engagement with bank leadership to ensure adherence to regulatory standards and prepare for risk-based supervision. Join us in fostering a secure and compliant banking environment for sustainable rural development.

[Status of KYC](kyc_page.html)

[Status of Pending Complaints](complaints_page.html)

[Status of Imbalance](imbalance_page.html)
"""

# HTML content for KYC page
kyc_page = """
<!DOCTYPE html>
<html>
<head>
    <title>KYC Banks</title>
</head>
<body>
    <h1>Status of KYC</h1>
    <ul>
        <li>AGRA DISTRICT CENTRAL CO-OPERATIVE BANK LTD.</li>
        <li>ALIGARH JILA SAHKARI BANK LTD.</li>
        <li>ALLAHABAD DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>BANDA DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>BIJNOR JILLA SAHKARI BANK LTD.</li>
        <li>BUDAUN JILLA SAHKARI BANK LTD.</li>
        <li>DISTRICT CO-OPERATIVE BANK LTD., VARANASI</li>
        <li>JILA SAHAKARI BANK LTD., MAU</li>
        <li>JILLA SAHKARI BANK LTD., BARABANKI</li>
        <li>JILLA SAHKARI BANK LTD., BAREILLY</li>
        <li>JILLA SAHKARI BANK LTD., BASTI</li>
        <li>JILLA SAHKARI BANK LTD., KANPUR</li>
        <li>JILLA SAHKARI BANK LTD., LUCKNOW.</li>
        <li>JILLA SAHKARI BANK LTD., MEERUT</li>
        <li>JILLA SAHKARI BANK LTD., MURADABAD</li>
        <li>JILLA SAHKARI BANK LTD., RAIBAREILLY</li>
        <li>JILLA SAHKARI BANK LTD., UNNAO</li>
        <li>MATHURA JILLA SAHKARI BANK LTD.</li>
        <li>PILIBHIT JILLA SAHKARI BANK LTD.</li>
        <li>BAHRICH DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>DEORIA KASIA CO-OPERATIVE BANK LTD.</li>
        <li>ETAWAH JILLA SAHKARI BANK LTD.</li>
        <li>FARRUKHABAD DISTRICT CO-OPERATIVE BANK LTD</li>
        <li>FATEHPUR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>FIROZABAD JILLA SAHKARI BANK LTD.</li>
        <li>GHAZIABAD JILLA SAHKARI BANK LTD.</li>
        <li>GORAKHPUR JILLA SAHKARI BANK LTD.</li>
        <li>HARDOI JILLA SAHKARI BANK LTD.</li>
        <li>JILLA SAHAKARI BANK LTD., AZAMGARH</li>
        <li>JILLA SAHKARI BANK LTD., BALLIA</li>
        <li>JILLA SAHKARI BANK LTD., JAUNPUR</li>
        <li>JILLA SAHKARI BANK LTD., JHANSI</li>
        <li>JILLA SAHKARI BANK LTD., LAKHIMPUR-KHIRI</li>
        <li>JILLA SAHKARI BANK LTD., MIRZAPUR</li>
        <li>JILLA SAHKARI BANK LTD., PRATAPGARH</li>
        <li>JILLA SAHKARI BANK LTD., SHAHJAHANPUR</li>
        <li>JILLA SAHKARI BANK LTD., SIDHARTHNAGAR</li>
        <li>JILLA SAHKARI BANK LTD., SITAPUR</li>
        <li>MAINPURI JILLA SAHKARI BANK LTD.</li>
        <li>MUZAFFARNAGAR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>RAMPUR JILLA SAHKARI BANK LTD.</li>
        <li>SULTANPUR JILLA SAHKARI BANK LTD.</li>
        <li>DISTRICT CO-OPERATIVE BANK LTD., SAHARANPUR</li>
        <li>ETAH DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>FAIZABAD JILLA SAHKARI BANK LTD.</li>
        <li>HAMIRPUR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>JALAUN DISTRICT CO-OERATIVE BANK LTD.</li>
        <li>JILLA SAHAKARI BANK LTD., GHAZIPUR</li>
        <li>JILLA SAHKARI BANK LTD., BULANDSAHAR</li>
        <li>JILLA SAHKARI BANK LTD., LALITPUR</li>
        <li>UTTAR PRADESH STATE COOPERATIVE BANK LTD., LUCKNOW</li>
        <li>PRATHAMA UP GRAMIN BANK</li>
        <li>BARODA UP BANK</li>
        <li>ARYAVART BANK</li>
        <li>UPSGVB</li>
    </ul>
</body>
</html>
"""
# HTML content for Complaints page
complaints_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Pending Complaints</title>
</head>
<body>
    <h1>Number of Pending complaints</h1>
    <ul>
        <li>AGRA DISTRICT CENTRAL CO-OPERATIVE BANK LTD.</li>
        <li>ALIGARH JILA SAHKARI BANK LTD.</li>
        <li>ALLAHABAD DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>BANDA DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>BIJNOR JILLA SAHKARI BANK LTD.</li>
        <li>BUDAUN JILLA SAHKARI BANK LTD.</li>
        <li>DISTRICT CO-OPERATIVE BANK LTD., VARANASI</li>
        <li>JILA SAHAKARI BANK LTD., MAU</li>
        <li>JILLA SAHKARI BANK LTD., BARABANKI</li>
        <li>JILLA SAHKARI BANK LTD., BAREILLY</li>
        <li>JILLA SAHKARI BANK LTD., BASTI</li>
        <li>JILLA SAHKARI BANK LTD., KANPUR</li>
        <li>JILLA SAHKARI BANK LTD., LUCKNOW.</li>
        <li>JILLA SAHKARI BANK LTD., MEERUT</li>
        <li>JILLA SAHKARI BANK LTD., MURADABAD</li>
        <li>JILLA SAHKARI BANK LTD., RAIBAREILLY</li>
        <li>JILLA SAHKARI BANK LTD., UNNAO</li>
        <li>MATHURA JILLA SAHKARI BANK LTD.</li>
        <li>PILIBHIT JILLA SAHKARI BANK LTD.</li>
        <li>BAHRICH DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>DEORIA KASIA CO-OPERATIVE BANK LTD.</li>
        <li>ETAWAH JILLA SAHKARI BANK LTD.</li>
        <li>FARRUKHABAD DISTRICT CO-OPERATIVE BANK LTD</li>
        <li>FATEHPUR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>FIROZABAD JILLA SAHKARI BANK LTD.</li>
        <li>GHAZIABAD JILLA SAHKARI BANK LTD.</li>
        <li>GORAKHPUR JILLA SAHKARI BANK LTD.</li>
        <li>HARDOI JILLA SAHKARI BANK LTD.</li>
        <li>JILLA SAHAKARI BANK LTD., AZAMGARH</li>
        <li>JILLA SAHKARI BANK LTD., BALLIA</li>
        <li>JILLA SAHKARI BANK LTD., JAUNPUR</li>
        <li>JILLA SAHKARI BANK LTD., JHANSI</li>
        <li>JILLA SAHKARI BANK LTD., LAKHIMPUR-KHIRI</li>
        <li>JILLA SAHKARI BANK LTD., MIRZAPUR</li>
        <li>JILLA SAHKARI BANK LTD., PRATAPGARH</li>
        <li>JILLA SAHKARI BANK LTD., SHAHJAHANPUR</li>
        <li>JILLA SAHKARI BANK LTD., SIDHARTHNAGAR</li>
        <li>JILLA SAHKARI BANK LTD., SITAPUR</li>
        <li>MAINPURI JILLA SAHKARI BANK LTD.</li>
        <li>MUZAFFARNAGAR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>RAMPUR JILLA SAHKARI BANK LTD.</li>
        <li>SULTANPUR JILLA SAHKARI BANK LTD.</li>
        <li>DISTRICT CO-OPERATIVE BANK LTD., SAHARANPUR</li>
        <li>ETAH DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>FAIZABAD JILLA SAHKARI BANK LTD.</li>
        <li>HAMIRPUR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>JALAUN DISTRICT CO-OERATIVE BANK LTD.</li>
        <li>JILLA SAHAKARI BANK LTD., GHAZIPUR</li>
        <li>JILLA SAHKARI BANK LTD., BULANDSAHAR</li>
        <li>JILLA SAHKARI BANK LTD., LALITPUR</li>
        <li>UTTAR PRADESH STATE COOPERATIVE BANK LTD., LUCKNOW</li>
        <li>PRATHAMA UP GRAMIN BANK</li>
        <li>BARODA UP BANK</li>
        <li>ARYAVART BANK</li>
        <li>UPSGVB</li>
    </ul>
</body>
</html>
"""

# HTML content for Imbalance page
imbalance_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Imbalance</title>
</head>
<body>
    <h1>Status of Imbalance</h1>
    <ul>
        <li>AGRA DISTRICT CENTRAL CO-OPERATIVE BANK LTD.</li>
        <li>ALIGARH JILA SAHKARI BANK LTD.</li>
        <li>ALLAHABAD DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>BANDA DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>BIJNOR JILLA SAHKARI BANK LTD.</li>
        <li>BUDAUN JILLA SAHKARI BANK LTD.</li>
        <li>DISTRICT CO-OPERATIVE BANK LTD., VARANASI</li>
        <li>JILA SAHAKARI BANK LTD., MAU</li>
        <li>JILLA SAHKARI BANK LTD., BARABANKI</li>
        <li>JILLA SAHKARI BANK LTD., BAREILLY</li>
        <li>JILLA SAHKARI BANK LTD., BASTI</li>
        <li>JILLA SAHKARI BANK LTD., KANPUR</li>
        <li>JILLA SAHKARI BANK LTD., LUCKNOW.</li>
        <li>JILLA SAHKARI BANK LTD., MEERUT</li>
        <li>JILLA SAHKARI BANK LTD., MURADABAD</li>
        <li>JILLA SAHKARI BANK LTD., RAIBAREILLY</li>
        <li>JILLA SAHKARI BANK LTD., UNNAO</li>
        <li>MATHURA JILLA SAHKARI BANK LTD.</li>
        <li>PILIBHIT JILLA SAHKARI BANK LTD.</li>
        <li>BAHRICH DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>DEORIA KASIA CO-OPERATIVE BANK LTD.</li>
        <li>ETAWAH JILLA SAHKARI BANK LTD.</li>
        <li>FARRUKHABAD DISTRICT CO-OPERATIVE BANK LTD</li>
        <li>FATEHPUR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>FIROZABAD JILLA SAHKARI BANK LTD.</li>
        <li>GHAZIABAD JILLA SAHKARI BANK LTD.</li>
        <li>GORAKHPUR JILLA SAHKARI BANK LTD.</li>
        <li>HARDOI JILLA SAHKARI BANK LTD.</li>
        <li>JILLA SAHAKARI BANK LTD., AZAMGARH</li>
        <li>JILLA SAHKARI BANK LTD., BALLIA</li>
        <li>JILLA SAHKARI BANK LTD., JAUNPUR</li>
        <li>JILLA SAHKARI BANK LTD., JHANSI</li>
        <li>JILLA SAHKARI BANK LTD., LAKHIMPUR-KHIRI</li>
        <li>JILLA SAHKARI BANK LTD., MIRZAPUR</li>
        <li>JILLA SAHKARI BANK LTD., PRATAPGARH</li>
        <li>JILLA SAHKARI BANK LTD., SHAHJAHANPUR</li>
        <li>JILLA SAHKARI BANK LTD., SIDHARTHNAGAR</li>
        <li>JILLA SAHKARI BANK LTD., SITAPUR</li>
        <li>MAINPURI JILLA SAHKARI BANK LTD.</li>
        <li>MUZAFFARNAGAR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>RAMPUR JILLA SAHKARI BANK LTD.</li>
        <li>SULTANPUR JILLA SAHKARI BANK LTD.</li>
        <li>DISTRICT CO-OPERATIVE BANK LTD., SAHARANPUR</li>
        <li>ETAH DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>FAIZABAD JILLA SAHKARI BANK LTD.</li>
        <li>HAMIRPUR DISTRICT CO-OPERATIVE BANK LTD.</li>
        <li>JALAUN DISTRICT CO-OERATIVE BANK LTD.</li>
        <li>JILLA SAHAKARI BANK LTD., GHAZIPUR</li>
        <li>JILLA SAHKARI BANK LTD., BULANDSAHAR</li>
        <li>JILLA SAHKARI BANK LTD., LALITPUR</li>
        <li>UTTAR PRADESH STATE COOPERATIVE BANK LTD., LUCKNOW</li>
        <li>PRATHAMA UP GRAMIN BANK</li>
        <li>BARODA UP BANK</li>
        <li>ARYAVART BANK</li>
        <li>UPSGVB</li>
    </ul>
</body>
</html>
"""


# Function to open page in web browser
def open_page(url):
    webbrowser.open_new(url)

if __name__ == "__main__":
    # Write the main page content to a file
    with open("main_page.html", "w") as f:
        f.write(main_page)
    
    # Write the KYC page content to a file
    with open("kyc_page.html", "w") as f:
        f.write(kyc_page)


    with open("complaints_page.html", "w") as f:
        f.write(complaints_page)

    with open("imbalance_page.html", "w") as f:
        f.write(imbalance_page)    
    # Set up GUI
    app = Gui("main_page.html")
    
    # Run the GUI
    app.run()
