
const {app,BrowserWindow}=require('electron')
const {exec}=require('child_process')

app.whenReady().then(()=>{

exec('uvicorn backend.main:app --port 8000')
exec('cd frontend && npm run dev')

const win=new BrowserWindow({width:1200,height:800})
win.loadURL('http://localhost:5173')

})
