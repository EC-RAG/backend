import{a as m}from"./axiosinstance-ChhllP2O.js";import{_ as te}from"./_plugin-vue_export-helper-DlAUqK2U.js";import{t as le}from"./index-BsqteGKW.js";import{i as d,j as oe,r as ne,k as T,c as a,d as t,e as u,F as se,o as h,g as C,u as I,R as re,b as ue,l as de,n as F,t as H,f as ie,m as n}from"./index-DiFkpt10.js";const ce=["onClick"],pe=["onClick"],me={__name:"alias",setup(ve){const{useToken:J}=le,{token:S}=J(),N=d([]),c=d(""),v=()=>{m.get("/api/data/gettabletags").then(l=>{N.value=l.data.map(e=>({label:e,value:e}))})};oe(()=>{v()});const P=[{title:"表名",dataIndex:"document",key:"document",width:200},{title:"别名",dataIndex:"id",key:"id",width:168},{title:"嵌入向量",dataIndex:"embedding",key:"embedding",ellipsis:!0},{title:"元数据",dataIndex:"metadata",key:"metadata",ellipsis:!0},{title:"操作",dataIndex:"edit",key:"edit",width:120}],_=d([]),U=()=>{s.value=!0,m.get("/api/data/gettablealias",{params:{table_name:c.value}}).then(l=>{console.log(l.data),_.value=l.data,_.value.forEach(e=>{e.embedding=JSON.stringify(e.embedding,null,2),e.metadata=JSON.stringify(e.metadata,null,2)}),n.success("查询成功"),s.value=!1}).catch(l=>{console.error(l),n.error("查询失败"),s.value=!1})},s=d(!1),V=l=>{navigator.clipboard.writeText(l).then(()=>{n.success("成功复制到剪切板")}).catch(e=>{console.error("复制失败:",e),n.error("复制失败")})},f=d(!1),r=ne({table_name:"",table_alias:""}),R={span:18},j={style:{width:"80px"}},A=()=>{f.value=!0},M=()=>{if(r.table_name===""){n.error("表名不能为空");return}if(r.table_alias===""){n.error("别名不能为空");return}s.value=!0,m.get("/api/data/addalias",{params:{table_name:r.table_name,table_alias:r.table_alias}}).then(l=>{n.success("添加成功"),r.table_name="",r.table_alias="",v(),f.value=!1,s.value=!1}).catch(l=>{console.error(l),n.error("添加失败"),s.value=!1})},G=l=>{s.value=!0,m.get("/api/data/rmalias",{params:{table_name:l.id}}).then(e=>{e.data===!0?(n.success("删除成功"),v(),U()):n.error("删除失败，请检查表名是否重复"),s.value=!1}).catch(e=>{console.error(e),n.error("删除失败"),s.value=!1})},K=()=>{s.value=!0,_.value=[],v(),c.value="",s.value=!1},w=d(!1),L=()=>{b.value=1,g.value="",y.value=[],w.value=!0},b=d(1),Q=[{label:"1",value:1},{label:"2",value:2},{label:"3",value:3},{label:"4",value:4},{label:"5",value:5}],W=[{title:"别名",dataIndex:"id",key:"id"},{title:"表名",dataIndex:"document",key:"document"},{title:"相似度",dataIndex:"distance",key:"distance",width:128}],y=d([]),x=d(!1),g=d(""),X=()=>{x.value=!0,y.value=[],m.get("/api/data/aliasquery",{params:{top_k:b.value,query:g.value}}).then(l=>{console.log(l.data),y.value=l.data,n.success("查询成功"),x.value=!1}).catch(l=>{console.error(l),n.error("查询失败"),x.value=!1})};return(l,e)=>{const O=u("a-select"),p=u("a-button"),i=u("a-layout-content"),B=u("a-card"),Y=u("a-popconfirm"),$=u("a-table"),q=u("a-input"),z=u("a-form-item"),Z=u("a-form"),D=u("a-modal"),ee=u("a-input-search");return h(),T(se,null,[a(i,{class:"main-content"},{default:t(()=>[a(B,{title:"别名管理",style:{width:"100%"},id:"title"},{default:t(()=>[a(i,{class:"search-box"},{default:t(()=>[a(i,{class:"left-box"},{default:t(()=>[a(O,{value:c.value,"onUpdate:value":e[0]||(e[0]=o=>c.value=o),style:{width:"100%"},placeholder:"表名",options:N.value},null,8,["value","options"]),a(p,{type:"primary",onClick:U,style:{"margin-left":"10px"},disabled:c.value==""},{default:t(()=>e[7]||(e[7]=[C("查询")])),_:1},8,["disabled"])]),_:1}),a(i,{class:"right-box"},{default:t(()=>[a(p,{type:"primary",onClick:A},{default:t(()=>e[8]||(e[8]=[C("添加数据")])),_:1}),a(p,{type:"primary",onClick:L},{default:t(()=>e[9]||(e[9]=[C("测试")])),_:1}),a(p,{type:"primary",onClick:K},{default:t(()=>[a(I(re))]),_:1})]),_:1})]),_:1})]),_:1}),a(B,{style:{width:"100%"}},{default:t(()=>[a($,{columns:P,"data-source":_.value,loading:s.value},{bodyCell:t(({column:o,text:k,record:ae})=>[o.dataIndex==="embedding"?(h(),T("span",{key:0,class:"copy",title:"点击复制",style:F({"--hover-color":I(S).colorPrimaryTextHover}),onClick:E=>V(k)},H(k),13,ce)):o.dataIndex==="metadata"?(h(),T("span",{key:1,class:"copy",title:"点击复制",style:F({"--hover-color":I(S).colorPrimaryTextHover}),onClick:E=>V(k)},H(k),13,pe)):o.dataIndex==="edit"?(h(),ue(Y,{key:2,title:"确定要删除这条数据吗？","cancel-text":"取消","ok-text":"提交",onConfirm:E=>G(ae)},{default:t(()=>[a(p,{type:"link",size:"small",danger:""},{default:t(()=>e[10]||(e[10]=[C("删除")])),_:1})]),_:2},1032,["onConfirm"])):de("",!0)]),_:1},8,["data-source","loading"])]),_:1})]),_:1}),a(D,{open:f.value,"onUpdate:open":e[3]||(e[3]=o=>f.value=o),title:"添加",onOk:M,width:"500px",cancelText:"取消",okText:"提交"},{default:t(()=>[a(Z,{model:r,"label-col":j,"wrapper-col":R,style:{"margin-top":"30px","margin-bottom":"30px"}},{default:t(()=>[a(z,{label:"表名"},{default:t(()=>[a(q,{value:r.table_name,"onUpdate:value":e[1]||(e[1]=o=>r.table_name=o)},null,8,["value"])]),_:1}),a(z,{label:"别名"},{default:t(()=>[a(q,{value:r.table_alias,"onUpdate:value":e[2]||(e[2]=o=>r.table_alias=o)},null,8,["value"])]),_:1})]),_:1},8,["model"])]),_:1},8,["open"]),a(D,{open:w.value,"onUpdate:open":e[6]||(e[6]=o=>w.value=o),title:"测试",width:"800px",footer:null},{default:t(()=>[a(i,{class:"test-search-box noselect"},{default:t(()=>[a(ee,{value:g.value,"onUpdate:value":e[4]||(e[4]=o=>g.value=o),placeholder:"请输入查询","allow-clear":!0,"enter-button":!0,onSearch:X,style:{width:"300px","margin-bottom":"20px",flex:"1","margin-top":"20px"}},null,8,["value"]),a(i,null,{default:t(()=>e[11]||(e[11]=[ie("span",null," 结果数 ",-1)])),_:1}),a(O,{ref:"select",value:b.value,"onUpdate:value":e[5]||(e[5]=o=>b.value=o),style:{width:"80px"},options:Q},null,8,["value"])]),_:1}),a($,{columns:W,"data-source":y.value,loading:x.value},null,8,["data-source","loading"])]),_:1},8,["open"])],64)}}},xe=te(me,[["__scopeId","data-v-3af43060"]]);export{xe as default};
