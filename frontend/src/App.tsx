
import {useEffect,useState} from 'react'

export default function App(){
const [d,setD]=useState<any>(null)

useEffect(()=>{
const ws=new WebSocket('ws://localhost:8000/ws')
ws.onmessage=(m)=>setD(JSON.parse(m.data))
return ()=>ws.close()
},[])

return (
<div style={{display:'flex'}}>
<div style={{width:'60%',background:'#111',color:'#0f0'}}>
<h3>MAP</h3>
<pre>{JSON.stringify(d?.map,null,2)}</pre>
</div>

<div style={{width:'40%'}}>
<h3>AI</h3>
<pre>{JSON.stringify(d?.ai,null,2)}</pre>
</div>
</div>
)
}
