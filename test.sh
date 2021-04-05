python tests/interfaces/testLogin.py >> test_goldens/Login.txt   
python tests/classes/testBuyRequests.py >> test_goldens/BuyRequests.txt  
python tests/classes/testSeller.py >> test_goldens/Seller.txt
python tests/classes/testBuyer.py >> test_goldens/Buyer.txt
python tests/classes/testUser.py >> test_goldens/User.txt  
python tests/classes/testManager.py >> test_goldens/Manager.txt  
python tests/classes/testitem.py >> test_goldens/Item.txt  
python tests/classes/testCustomer.py >> test_goldens/Customer.txt  
python tests/classes/testCategory.py >> test_goldens/Category.txt  
python tests/classes/testAddress.py >> test_goldens/Address.txt  

python tests/interfaces/testLogin.py >> test_outputs/Login.txt   
echo "Testing Login"
if  cmp -s  test_outputs/Login.txt test_goldens/Login.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi 

python tests/classes/testBuyRequests.py >> test_outputs/BuyRequests.txt  
echo "Testing Buy Requests"
if  cmp -s  test_outputs/BuyRequests.txt test_goldens/BuyRequests.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi
python tests/classes/testSeller.py >> test_outputs/Seller.txt
echo "Testing Seller"
if  cmp -s  test_outputs/Seller.txt test_goldens/Seller.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi
python tests/classes/testBuyer.py >> test_outputs/Buyer.txt
echo "Testing Buyer"
if  cmp -s  test_outputs/Buyer.txt test_goldens/Buyer.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi
python tests/classes/testUser.py >> test_outputs/User.txt  
echo "Testing User"
if  cmp -s  test_outputs/User.txt test_goldens/User.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi
python tests/classes/testManager.py >> test_outputs/Manager.txt  
echo "Testing Manager"
if  cmp -s  test_outputs/Manager.txt test_goldens/Manager.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi
python tests/classes/testitem.py >> test_outputs/Item.txt  
echo "Testing Item"
if  cmp -s  test_outputs/Item.txt test_goldens/Item.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi
python tests/classes/testCustomer.py >> test_outputs/Customer.txt  
echo "Testing Customer"
if  cmp -s  test_outputs/Customer.txt test_goldens/Customer.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi
python tests/classes/testCategory.py >> test_outputs/Category.txt  
echo "Testing Category"
if  cmp -s  test_outputs/Category.txt test_goldens/Category.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi
python tests/classes/testAddress.py >> test_outputs/Address.txt  
echo "Testing Address"
if  cmp -s  test_outputs/Address.txt test_goldens/Address.txt  
then 
    echo $'\n Matches golden, unit tests passed !! \n'
else
    echo $'\n Doesnt Match golden, unit tests FAILED :( !! \n'
fi