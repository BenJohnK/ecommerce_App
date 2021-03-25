var button_elements=document.getElementsByClassName('add-button')
for(i=0;i<button_elements.length;i++){
    button_elements[i].addEventListener('click',function(){
        productid=this.getAttribute('productid')
        action=this.getAttribute('action')
        var url='/update_cart/'
        fetch(url,{
            'method':'POST',
            'headers':{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken
            },
            'body':JSON.stringify({'productid':productid,'action':action}),
        })
        .then((response)=>{
            return response.json()
        })
        .then((data)=>{
            console.log(data);
            window.location.reload();
        })
    })
}
