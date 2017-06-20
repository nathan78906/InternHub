function readTextFile(file){
    var str = "";
    // Get the user info as XML HTTP Request object
    var textInfoXMLHttpRequest = new XMLHttpRequest();
    textInfoXMLHttpRequest.open("GET", file, false);
    textInfoXMLHttpRequest.onreadystatechange = function() {
    // Check if the file is ready
    if(textInfoXMLHttpRequest.readyState === 4){
        // Check the status and type 
        if(textInfoXMLHttpRequest.status === 200 || textInfoXMLHttpRequest.status == 0){
            // Variable that has text as string
            var allText = textInfoXMLHttpRequest.responseText;
            str = allText;  
            }
        }
    };
	textInfoXMLHttpRequest.send(null);
    return str;
}
/*
Given a string of characters everyUserInfo, return
an array sliptInfo where each element is a string
of username and passwords seperated by a comma.
*/
function getArrayOfUsers(everyUserInfo){
    // Split the text by new line
    var splitInfo = everyUserInfo.split('\n');
    // Return the split info so that each
    // username and password can be checked
    return splitInfo;
}
/*
Returns true if the username and password entered
matched a username and password in the text file.
Otherwise it returns false.
*/
function verifyLogin(splitInfo){
    // Initialize a that the username and
    // password entered is false as a variable
    var result = false;
    // Get user input value for username
    var givenUsername = document.getElementById("textUsername").value;
    // Get user input value for password
    var givenPassword = document.getElementById("textPassword").value;
    for (var i = 0; i < splitInfo.length; i++) {
        if (splitInfo[i].localeCompare(givenUsername + "," + givenPassword) == 0){
            result = true;
        }
    }
    // Return the result of the verification
    return result;
}
/*
Alrets the user that the username and password given
is valid/invalid.
*/
function displayVerification(){
    // TODO: Make sure the path of student home page is correct
    var filePath = "file:///Better-Jobs/Better_Jobs/Student%20Home%20Page/studentHP.html";
    var userInfoTextPath = "file:///Better-Jobs/Better_Jobs/info.txt";
    // TODO: If above is correct the rest should work
    var userInfo = getArrayOfUsers(readTextFile(userInfoTextPath);
    // Check if information entered is correct
    // Otherwise tell the user that the info is invalid
    if(verifyLogin(userInfo)){
        // Display to the user that info is valid
        window.location.href = filePath;
    }else{
        alert("Invalid!")
    }
}

