<!DOCTYPE html>
addMsg('You', text);
const r = await fetch('/.netlify/functions/chat',{
method:'POST',
body: JSON.stringify({prompt:text})
});
const out = await r.json();
addMsg('Black I', out.reply);
if(out.video){ addVideo(out.video); }
}
});


function addMsg(who, msg){
const m=document.createElement('div');
m.className='box';
m.innerText=who+': '+msg;
document.getElementById('messages').appendChild(m);
}
function addVideo(url){
const v=document.createElement('video');
v.src=url;
v.controls=true;
document.getElementById('messages').appendChild(v);
}
</script>
</body>
</html>




<!-- netlify/functions/chat.js -->
exports.handler = async (event) => {
const body = JSON.parse(event.body);
const prompt = body.prompt;


const openai = await fetch("https://api.openai.com/v1/chat/completions",{
method:"POST",
headers:{
"Content-Type":"application/json",
"Authorization":`Bearer ${process.env.OPENAI_API_KEY}`
},
body: JSON.stringify({
model:"gpt-4o-mini",
messages:[{role:"user",content:prompt}]
})
});
const data = await openai.json();
const reply = data.choices[0].message.content;


const videoURL = null;


return {
statusCode: 200,
body: JSON.stringify({reply:reply, video:videoURL})
};
};




<!-- netlify.toml -->
[build]
functions = "netlify/functions"
publish = "/"




<!-- package.json -->
{
"name": "black-i-prototype1",
"version": "1.0.0",
"dependencies": {}
}




<!-- README -->
Use Netlify → New site → drag folder.
Add env var: OPENAI_API_KEY.