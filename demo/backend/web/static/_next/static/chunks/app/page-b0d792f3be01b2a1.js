(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[931],{76032:function(e,t,s){Promise.resolve().then(s.bind(s,94096))},94096:function(e,t,s){"use strict";s.r(t),s.d(t,{default:function(){return h}});var a=s(57437),l=s(2265),o=s(39343),r=s(90632),n=s(68396),i=s(20124),c=s(27485),d=s(45023),m=e=>{let{modelTime:t,queryTime:s,queryResults:o}=e,r=[];for(let e=0;e<o[0].length;e++){let t={accessorKey:"col-#-".concat(e),header:"col-#-".concat(e),muiTableBodyCellProps:{align:"center"},muiTableHeadCellProps:{align:"center"}};r.push(t)}let n=(0,l.useMemo)(()=>r,[o,r]),i=(0,l.useMemo)(()=>{let e=Array(o.length);return o.forEach((t,s)=>{let a={};t.forEach((e,t)=>{a["col-#-".concat(t)]=e.toString()}),e[s]=a}),e},[o]),c=(0,d.X0)({columns:n,data:i,enableKeyboardShortcuts:!1,enableColumnActions:!1,enableColumnFilters:!1,enableTopToolbar:!1,enablePagination:!0,enableSorting:!1,positionPagination:"both",muiPaginationProps:{color:"secondary",shape:"rounded",showRowsPerPage:!0},muiTableBodyRowProps:{hover:!1},mrtTheme:()=>({baseBackgroundColor:"#1F2041"}),muiTableProps:{sx:{border:"1px solid rgba(81, 81, 81, .5)",caption:{captionSide:"top"},color:"white"}},muiTableHeadCellProps:{sx:{border:"1px solid rgba(81, 81, 81, .5)",fontWeight:"bold",color:"white",backgroundColor:"#4B3F72"}},muiTableBodyCellProps:{sx:{border:"1px solid rgba(81, 81, 81, .5)",color:"white"}},renderCaption:e=>{let{table:a}=e;return"Model Time: ".concat(t.toFixed(2)," seconds || Query Time: ").concat(s.toFixed(2)," seconds")}});return(0,a.jsx)(d.P2,{table:c})};let u=(0,r.Z)({palette:{mode:"dark"}}),x=[{num:1,question:"What is the highest bytesSent for server baz?",context:"CREATE TABLE head (name VARCHAR, born_state VARCHAR, age VARCHAR)"},{num:2,context:"CREATE TABLE IF NOT EXISTS devices (device_id INTEGER, ts TIMESTAMP, co DOUBLE, humidity DOUBLE,light BOOL,lpg DOUBLE,motion BOOL,smoke DOUBLE,temp DOUBLE);",question:"What is the average contentLength in March 9, 2009 for the server foo?"},{num:3,context:"CREATE TABLE IF NOT EXISTS iot_meter_foo (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE); CREATE TABLE IF NOT EXISTS iot_meter_bar (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE); CREATE TABLE IF NOT EXISTS iot_meter_baz (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE);",question:"How many status code 404 on server bar on April 4, 2010?"}];function h(){let[e,t]=l.useState(""),[s,r]=l.useState(!1),[d,h]=l.useState([]),[p,b]=l.useState(0),[g,E]=l.useState(0),[f,y]=l.useState(!1),{register:T,handleSubmit:j,formState:{errors:N}}=(0,o.cI)();return(0,a.jsxs)(n.Z,{theme:u,children:[(0,a.jsx)(i.ZP,{}),(0,a.jsxs)("button",{className:"p-2 absolute left-0 top-24 bg-gray-400 rounded-r-lg  bg-gray-300 cursor-pointer text-align-center",style:{display:s?"none":"block"},onClick:()=>r(!s),children:[(0,a.jsx)("span",{className:"text-slate-900",children:" Show "}),(0,a.jsx)("br",{}),"  ",(0,a.jsx)("span",{className:"text-slate-900",children:" Examples"})]}),(0,a.jsx)("div",{className:"absolute left-0 top-24 bg-gray-400 max-w-96 rounded-sm z-20",style:{display:s?"block":"none"},children:(0,a.jsxs)("div",{className:"m-5",children:[(0,a.jsx)("button",{className:"absolute top-0 right-0 m-1 px-2 py-1 border border-gray-600 cursor-pointer bg-gray-500",onClick:()=>r(!s),children:"X"}),(0,a.jsx)("span",{className:"text-2xl text-slate-900",children:" Examples "}),(0,a.jsx)("ol",{className:"text-md text-slate-800",children:x.map(e=>(0,a.jsx)("div",{className:"mx-2 my-6 border border-dotted",children:(0,a.jsxs)("li",{className:"m-2",children:[(0,a.jsx)("span",{className:"underline",children:"question:"}),"  ",(0,a.jsxs)("span",{className:"font-semibold",children:[" ",e.question," "]})]})},e.num))})]})}),(0,a.jsxs)("main",{className:"flex min-h-screen flex-col items-center justify-start p-24",children:[(0,a.jsxs)("div",{className:"flex w-full max-w-5xl items-center lg:flex justify-around",style:{opacity:f?"0.5":"1"},children:[(0,a.jsxs)("div",{className:"flex-col",children:[(0,a.jsx)("h1",{className:"text-neutral-200 my-5 text-xl justify-center",children:" Ask A Question "}),(0,a.jsxs)("form",{onSubmit:j(e=>{console.log(e),y(!0),fetch("".concat("/nlquery","?question=").concat(e.question),{method:"GET",mode:"no-cors",cache:"no-cache"}).then(e=>e.json()).then(e=>{t(e.query),b(e.model_time),E(e.query_time),h(e.results),console.log(e),y(!1)})}),children:[(0,a.jsxs)("section",{className:"flex flex-col justify-center align-center gap-4",children:[(0,a.jsx)("textarea",{className:"text-stone-950 p-2 w-80 h-20",defaultValue:"What is the highest bytesSent for server baz?",...T("question",{required:!0})}),N.question&&(0,a.jsx)("span",{children:"This field is required"})]}),(0,a.jsx)("section",{className:"flex justify-center",children:(0,a.jsx)("input",{className:"bg-slate-600 px-3 py-2 my-4 rounded-md cursor-pointer",type:"submit"})})]})]}),(0,a.jsxs)("div",{className:"flex-col",children:[(0,a.jsx)("h3",{className:"text-neutral-200 my-5 text-xl justify-center",children:" Generated SQL Query"}),(0,a.jsx)("div",{className:"bg-stone-900 rounded-md p-6  border border-slate-600 shadow-lg shadow-indigo-500/40 my-5 min-w-96 hover:z-50 ",children:(0,a.jsxs)("pre",{className:"text-blue-300 my-6 text-xl font-semibold leading-8 max-h-64 max-w-2xl overflow-auto whitespace-pre-wrap ",children:[" ",e," "]})})]})]}),(0,a.jsxs)("div",{className:"flex-col w-full my-5 max-w-5xl lg:flex item-center",children:[f?(0,a.jsx)(c.Yt,{visible:!0,height:"300",width:"300",ariaLabel:"magnifying-glass-loading",wrapperStyle:{},wrapperClass:"magnifying-glass-wrapper",glassColor:"#c0efff",color:"#e15b64"}):(0,a.jsx)(a.Fragment,{}),d.length>0?(0,a.jsx)(m,{queryResults:d,modelTime:p,queryTime:g}):(0,a.jsx)(a.Fragment,{})]})]})]})}}},function(e){e.O(0,[571,712,440,971,23,744],function(){return e(e.s=76032)}),_N_E=e.O()}]);