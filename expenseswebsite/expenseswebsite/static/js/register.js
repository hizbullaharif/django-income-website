const usernameField= document.querySelector('#username');
const feedbackAreaUser= document.querySelector('.invalid_feedbackuser');
const feedbackAreaEmail= document.querySelector('.invalid_feedbackemail');
const emailField = document.querySelector('#useremail');


// username validation
usernameField.addEventListener('keyup', (e)=>{
    const usernameval= e.target.value;

    usernameField.classList.remove("is-invalid");
    feedbackAreaUser.style.display="none";
    if (usernameval.length > 0){
        fetch("validate-username",{
            body:JSON.stringify({username:usernameval}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            
            if(data.username_error){
                usernameField.classList.add("is-invalid");
                feedbackAreaUser.style.display='block';
                feedbackAreaUser.innerHTML= '<p>'+data.username_error+'</p>';
            }
        })
    }

});

//email validation

emailField.addEventListener('keyup', (e)=>{
    const emailval= e.target.value;
   
    emailField.classList.remove("is-invalid");
feedbackAreaEmail.style.display="none";
    if (emailval.length > 0){
        fetch("validate-email",{
            body:JSON.stringify({email:emailval}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            
            if(data.email_error){
                emailField.classList.add("is-invalid");
                feedbackAreaEmail.style.display='block';
                feedbackAreaEmail.innerHTML= '<p>'+data.email_error+'</p>';
            }
        })
    }

});