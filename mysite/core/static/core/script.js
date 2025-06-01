function greetUser(){
    alert("Hello from django and python");
}

function toggleTheme(){
    const body=document.body;
    body.classList.toggle('dark-theme');
    if (body.classList.contains('dark-theme')){
        localStorage.setItem('theme','dark');
    }else{
        localStorage.setItem('theme','light')
    }
}

window.onload=() =>
{
    const savedTheme=localStorage.getItem('theme');
    if(savedTheme=='dark')
    {
        document.body.classList.add('dark-theme')
    }
}