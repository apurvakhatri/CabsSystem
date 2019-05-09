Post: http://localhost:8000/createDriver/  
{  
	"password":"pbj135",  
	"last_login":"2019-05-06 06:00Z",  
	"is_superuser":false, 
	"username":"santacruz_station_driver", 
	"first_name":"grappus",
	"last_name":"gurgaon", 
	"email":"apurva@grappus.com", 
	"is_staff":false,
	"is_active":true,
	"date_joined":"2019-05-06 06:00Z", 
	"contact_number":1159022257,
	"country":"India",
	"state":"Haryana", 
	"city":"Gurgaon", 
	"address":"SS Plaza", 
	"pincode":985873, 
	"type":"DR",
	"country_code":"91", 
	"license_number":"ABCDEFGH1234", 
	"car_number":"MH-02-EA-6204",
	"working":true,
	"status":true,
	"latitude":19.079792,
	"longitude":72.846819,
	"rating":10
}

Post: http://localhost:8000/createCustomer/
{
	"password":"pbj135", 
	"last_login":"2019-05-06 06:00Z",
	"is_superuser":false, 
	"username":"grappusgurgaon29", 
	"first_name":"grappus",
	"last_name":"gurgaon", 
	"email":"apurva@grappus.com", 
	"is_staff":false,
	"is_active":true,
	"date_joined":"2019-05-06 06:00Z", 
	"contact_number":1159022257,
	"country":"India",
	"state":"Haryana", 
	"city":"Gurgaon", 
	"address":"SS Plaza", 
	"pincode":985873, 
	"type”:”C”,
	"Upi_id":"apurva@okicici"
}

Get: http://localhost:8000/driver/
Return: All driver objects

Get: http://localhost:8000/customer/
Return: All customer objects

Get: http://localhost:8000/customer/{insert id here}/
Return: Details of the particular customer

Get: http://localhost:8000/book/{insert id here}/{insert latitude}/{insert longitude}/
Examples: http://localhost:8000/book/899c1a51-b7e8-4892-bbee-bc285278e2f9/28.552989/77.122044/
Return: driver object