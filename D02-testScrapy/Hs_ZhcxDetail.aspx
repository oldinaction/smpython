

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <script src="../JS/jquery.min.js" type="text/javascript"></script>
    <script src="../JS/jquery.easyui.min.js" type="text/javascript"></script>
    <script src="../JS/jquery.popup.js" type="text/javascript"></script>
    <title>

</title>
    <script type="text/javascript">
        function Show(type) {
            if (type == "hgjg") {
                var conditions = document.getElementById("acustom").innerHTML;
            }
            else {
                var conditions = document.getElementById("aClass").innerHTML;
            }
            $("#Iframepara").attr("src", "Search_Para.aspx?checksty=" + conditions + "&type=" + type);
            $('#divSearchpara').window("open");
        }

        function TanChu(type) {
            var hspcode = document.getElementById("lbpscode").innerText;
            $("#IframeTanchu").attr("src", "Tanchu.aspx?spbm=" + hspcode + "&type=" + type);
            $("#divTanchu").window("open");
        }
        function ITA() {
            var hspcode = document.getElementById("lbpscode").innerText;
            $("#IframeITA").attr("src", "HS_ITA.aspx?spbm=" + hspcode);
            $('#divITA').window("open");
        }
        function Fuhe() {
            var hspcode = document.getElementById("lbpscode").innerText;
            $("#IframeFuhe").attr("src", "HS_Fuhe.aspx?spbm=" + hspcode);
            $('#divFuhe').window("open");
        }
        function closeWindow() {
            $.popup.close("#IframeZhcxDetail");
        }
        function closewinTanchu() {
            //$.popup.close("#divTanchu");
            $("#divTanchu").window("close");
        }
        function closewinITA() {
            $("#divITA").window("close");
            //$.popup.close("#divITA");
        }
        function closewinFuhe() {
            $("#divFuhe").window("close");
            //$.popup.close("#divFuhe");
        }
    </script>

<script language="Javascript">
    document.oncontextmenu = new Function("event.returnValue=false");
    document.onselectstart = new Function("event.returnValue=false");
</script> 



    <style type="text/css">
        .td {
            border-right-style: solid;
            border-bottom-style: solid;
            border-right-width: 1px;
            border-bottom-width: 1px;
            border-right-color: #DADADA;
            border-bottom-color: #DADADA;
            text-align: center;
        }

        .td2 {
            border-bottom-style: solid;
            border-bottom-width: 1px;
            border-bottom-color: #DADADA;
            text-align: center;
        }
    </style>
</head>
<body>
    <form method="post" action="Hs_ZhcxDetail.aspx?spbm=7616999000" id="form1">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTEwMDY0MjkzMzgPZBYCAgMPZBYuAgEPDxYCHgRUZXh0BQo3NjE2OTk5MDAwZGQCAw8PFgIfAAUG5Y2D5YWLZGQCBQ8PFgIfAAUb5YW25LuW6Z2e5bel5Lia55So6ZOd5Yi25ZOBZGQCBw8PFgIfAAVyT3RoZXIgYXJ0aWNsZXMgb2YgYWx1bWluaXVtLCBub3QgZm9yIHRlY2huaWNhbCB1c2UsIGV4Y2x1ZGluZyBjbG90aCwgZ3JpbGwsIG5ldHRpbmcgYW5kIGZlbmNpbmcsIG9mIGFsdW1pbml1bSB3aXJlZGQCCQ8PFgIfAAWkATHlk4HlkI07MijnlKjpgJRb5bel5Lia55So44CB6Z2e5bel5Lia55SoXSk7MyjmnZDotKhb6ZOdXSk7NCjnp43nsbtb5Zu+6ZKJ44CB6J666ZKJ44CB5biD44CB572R44CB56+x562JXSk7NSjlhbbku5Zb6Z2e5b+F5oql6KaB57Sg77yM6K+35qC55o2u5a6e6ZmF5oOF5Ya15aGr5oqlXSk7ZGQCCw8PFgIfAAVvMS7nlKjpgJTvvIjlt6XkuJrnlKjjgIHpnZ7lt6XkuJrnlKjvvInvvJsyLuadkOi0qO+8iOmTne+8ie+8mzMu56eN57G777yI5Zu+6ZKJ44CB6J666ZKJ44CB5biD44CB572R44CB56+x562J77yJZGQCDQ8PFgIfAAUCMTVkZAIPDw8WAh8ABQPml6BkZAIRDw8WAh8ABQI4MGRkAhMPDxYCHwAFAjE3ZGQCFw8WAh4JaW5uZXJodG1sBQPmnIlkAhsPFgIfAQUD5pyJZAIdDw8WAh8ABQPml6BkZAIhDw8WAh8ABQPml6BkZAIlDw8WAh8ABQPml6BkZAIpDw8WAh8ABQPml6BkZAItDw8WAh8ABQEwZGQCLw8PFgIfAAUEMTMuMGRkAjEPDxYCHwAFA+aXoGRkAjMPDxYCHwAFA+aXoGRkAjcPDxYCHwAFA+aXoGRkAj0PFgQfAQUD5pyJHgRocmVmBVBodHRwOi8vd3d3LjUyeGluaGFpLmNvbS9IU0RpY3Rpb25hcnkvVXBsb2FkRmlsZS9vcmlnaW5hbC8yMDEzMDEveGh5eTIwMTItMDExLmpwZ2QCQQ8WBB8BBQPmnIkfAgUjUGlubWluZ19saXN0LmFzcHg/aHNjb2RlPTc2MTY5OTkwMDBkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQlidG5DbG9zZTEFDEltYWdlQnV0dG9uMQUMSW1hZ2VCdXR0b24ydO6PHurDbLUMNIdOZjXSw1Ug9dwunVfDIxiNTv9hxSs=" />
</div>

<div class="aspNetHidden">

	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAAQCp1OioMxNaS6K7LsblreK98Ct771XrSvx8bU25uvPxOmQAq8eUWZ5ZSknq1PiLipizVftpmYJzgJTRuQ1U4NbNlY+yJGjQMsZUUYJnMCmOIE9AVzMNuXrlIIg2lSkNh4=" />
</div>
        <div>
            <table style="border: 1px solid #959595; width: 100%;" cellspacing="0">
                <tr>
                    <td rowspan="4" class="td" style="width: 136px; height: 40px; font-family: 黑体; font-weight: bold; font-size: 16px; color: #21686b;">申报信息</td>
                    <td class="td" style="width: 136px; height: 40px; font-family: 微软雅黑; font-size: 14px; color: #2a959a;">商品编码</td>
                    <td class="td" style="width: 136px; height: 40px; text-align:left;padding-left:5px" colspan="5">
                        <span id="lbpscode" style="color:#EA712F;font-family:微软雅黑;font-size:14px;">7616999000</span>
                    </td>
                    <td class="td" style="width: 136px; height: 40px; font-family: 微软雅黑; font-size: 14px; color: #2a959a;">计量单位</td>

                    <td class="td2" style="width: 136px; height: 40px;text-align:left;padding-left:5px" colspan="5">
                        <span id="lbunit" style="color:#3E4040;font-family:微软雅黑;font-size:14px;">千克</span>
                    </td>
                </tr>
                <tr>
                    <td class="td" style="font-family: 微软雅黑; font-size: 14px; color: #2a959a;">商品名称</td>
                    <td class="td" style="width: 136px; height: 70px;text-align:left;padding-left:5px" colspan="5">
                        <span id="lbspname" style="color:#3E4040;font-family:微软雅黑;font-size:14px;">其他非工业用铝制品</span>
                    </td>
                    <td class="td" style="width: 136px; height: 70px; font-family: 微软雅黑; font-size: 14px; color: #2a959a;">英文名称</td>
                    <td class="td2" style="width: 136px; height: 70px;text-align:left;padding-left:5px" colspan="5">
                        <span id="lbenglishname" style="color:#3E4040;font-family:Arial;font-size:12px;">Other articles of aluminium, not for technical use, excluding cloth, grill, netting and fencing, of aluminium wire</span>
                    </td>
                </tr>
                <tr>
                    <td class="td" rowspan="2" style="width: 136px; height: 70px; font-family: 微软雅黑; font-size: 14px; color: #2a959a;">申报要素</td>
                    <td class="td" style="width: 136px; height: 70px; font-family: 微软雅黑; font-size: 14px; color: #2a959a;">上海版</td>
                    <td class="td2" colspan="10" style="height: 70px;text-align:left;padding-left:5px">
                        <span id="lbsbys" style="color:#3E4040;font-family:微软雅黑;font-size:14px;">1品名;2(用途[工业用、非工业用]);3(材质[铝]);4(种类[图钉、螺钉、布、网、篱等]);5(其他[非必报要素，请根据实际情况填报]);</span>
                    </td>
                </tr>
                <tr>
                    <td class="td" style="width: 136px; height: 70px; font-family: 微软雅黑; font-size: 14px; color: #2a959a;">全国版</td>
                    <td class="td2" colspan="10" style="height: 70px;text-align:left;padding-left:5px">
                        <span id="lbsbysqgb" style="color:#3E4040;font-family:微软雅黑;font-size:14px;">1.用途（工业用、非工业用）；2.材质（铝）；3.种类（图钉、螺钉、布、网、篱等）</span>
                    </td>
                </tr>
                <tr>
                    <td rowspan="3" class="td" style="font-family: 黑体; font-size: 16px; font-weight: bold; color: #21686b;">税费信息</td>
                    <td rowspan="2" class="td" style="font-family: 微软雅黑; font-size: 14px; color: #2a959a;">进口</td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">最惠国税率(%)</td>
                    <td class="td" style="width: 40px; height: 40px;">
                        <span id="lbzuihui" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">15</span>
                    </td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">暂定税(%)</td>
                    <td class="td" style="width: 40px; height: 40px;">
                        <span id="lbzanding" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">无</span>
                    </td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">普通税率(%)</td>
                    <td class="td" style="width: 40px; height: 40px;">
                        <span id="lbputong" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">80</span>
                    </td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">增值税(%)</td>
                    <td class="td" style="width: 40px; height: 40px;">
                        <span id="lbzengzhi" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">17</span>
                    </td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">协定税率(%)</td>
                    <td class="td2" style="width: 40px; height: 40px;">
                        <span id="lbxieding" style="color:#2A3193;font-family:微软雅黑;font-size:14px;"></span>
                        <a id="aXieding" onclick="TanChu(&#39;xieding&#39;)" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;">有</a>
                    </td>
                </tr>
                <tr>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">特惠税率(%)</td>
                    <td class="td" style="width: 40px; height: 40px;">
                        <span id="lbtehui" style="color:#2A3193;font-family:微软雅黑;font-size:14px;"></span>
                        <a id="aTehui" onclick="TanChu(&#39;tehui&#39;)" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;">有</a>
                    </td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">消费税率(%)</td>
                    <td class="td" style="width: 40px; height: 40px;">
                        <span id="lbxiaofei" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">无</span>
                        <a id="axiaofei" onclick="TanChu(&#39;xiaofei&#39;)" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;"></a>
                    </td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">复合从量(%)</td>
                    <td class="td" style="width: 40px; height: 40px;">
                        <span id="lbfuhe" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">无</span>
                        <a id="aFuHe" onclick="Fuhe()" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;"></a>
                    </td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">双反税率(%)</td>
                    <td class="td" style="width: 40px; height: 40px;">
                        <span id="lbfanqingxiao" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">无</span>
                        <a id="aFanQingXiao" target="_blank" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;"></a>
                    </td>
                    <td class="td" style="width: 180px; height: 40px; font-family: 微软雅黑; font-size: 14px;">ITA税率(%)</td>
                    <td class="td2" style="width: 40px; height: 40px;">
                        <span id="lbita" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">无</span>
                        <a id="aIta" onclick="ITA()" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;"></a>
                    </td>
                </tr>
                <tr>
                    <td class="td" style="font-family: 微软雅黑; font-size: 14px; color: #2a959a;">出口</td>
                    <td class="td" style="width: 136px; height: 70px; font-family: 微软雅黑; font-size: 14px;" colspan="2">税率(%)</td>
                    <td class="td" style="width: 136px; height: 70px;">
                        <span id="lbchukou" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">0</span>
                    </td>
                    <td class="td" style="width: 136px; height: 70px; font-family: 微软雅黑; font-size: 14px;" colspan="2">退税(%)</td>
                    <td class="td" style="width: 136px; height: 70px; font-family: 微软雅黑; font-size: 14px; color: #2a959a;">
                        <span id="lbchukoutuishui" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">13.0</span>
                    </td>
                    <td class="td" style="width: 136px; height: 70px; font-family: 微软雅黑; font-size: 14px;" colspan="2">暂定税率(%)</td>
                    <td class="td2" style="width: 136px; height: 70px;" colspan="2">
                        <span id="lbchukouzanding" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">无</span>
                    </td>
                </tr>
                <tr>
                    <td class="td" style="font-family: 黑体; font-size: 16px; color: #21686b; font-weight: bold;">监管信息</td>
                    <td class="td" style="width: 136px; height: 60px; font-family: 微软雅黑; font-size: 14px;" colspan="5">海关监管条件</td>
                    <td class="td" style="width: 136px; height: 60px;">
                        <span id="lbcustom" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">无</span>
                        <a id="acustom" class="tanchu" onclick="Show(&#39;hgjg&#39;)" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;"></a>
                    </td>
                    <td class="td" style="width: 136px; height: 60px; font-family: 微软雅黑; font-size: 14px;" colspan="4">检验检疫类别</td>
                    <td class="td2" style="width: 136px; height: 60px;">
                        <span id="lbClass" style="color:#2A3193;font-family:微软雅黑;font-size:14px;">无</span>
                        <a id="aClass" class="tanchu" onclick="Show(&#39;jyjylb&#39;)" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;"></a>
                    </td>
                </tr>
                <tr>
                    <td class="td" style="font-family: 黑体; font-size: 16px; color: #21686b; font-weight: bold;">参考信息</td>
                    <td class="td" style="width: 136px; height: 60px; font-family: 微软雅黑; font-size: 14px;" colspan="5">图片库</td>
                    <td class="td">
                        <span id="lbtupian" style="color:#2A3193;font-family:微软雅黑;font-size:14px;"></span>
                        <a href="http://www.52xinhai.com/HSDictionary/UploadFile/original/201301/xhyy2012-011.jpg" id="tupianku" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;" target="_blank">有</a>
                    </td>
                    <td class="td" style="width: 136px; height: 60px; font-family: 微软雅黑; font-size: 14px;" colspan="4">历史库</td>
                    <td class="td2">
                        <span id="lblishi" style="color:#2A3193;font-family:微软雅黑;font-size:14px;"></span>
                        <a href="Pinming_list.aspx?hscode=7616999000" id="aLiShi" style="cursor: pointer; color: #ea712f; font-size: 12px; font-family: Arial; text-decoration: underline; border: none; text-align: left; vertical-align: middle; line-height: 25pt;" target="_blank">有</a>
                    </td>
                </tr>
            </table>
        </div>
        <div id="divSearchpara" style="position: absolute; top: 15%; left: 30%; width: 400px; height: 300px; background-color: white; border: 1px solid #959595;"
            class="easyui-window" title=" " closed="true" collapsible="false" minimizable="false" maximizable="false" closable="false">
            <iframe id="Iframepara" style="width: 100%; height: 100%; border-style: none;"></iframe>
        </div>

        <div id="divTanchu" style=" position: absolute; top: 4%; left: 45%; width: 450px; height: 500px; background-color: white; border: 1px solid #959595;"
            class="easyui-window" title=" " closed="true" collapsible="false" minimizable="false" maximizable="false" closable="false">
            <div style="text-align: right;">
                <input type="image" name="btnClose1" id="btnClose1" src="../Images/ButtonClose.png" onclick="closewinTanchu();" style="height:15px;width:15px;" />
            </div>
            <iframe id="IframeTanchu" style="width: 100%; height: 450px; border-style: none;"></iframe>
        </div>

        <div id="divITA" style=" position: absolute; top: 15%; left: 35%; width: 350px; height: 240px; background-color: white; border: 1px solid #959595;"
            class="easyui-window" title=" " closed="true" collapsible="false" minimizable="false" maximizable="false" closable="false">
            <div style="text-align: right;">
                <input type="image" name="ImageButton1" id="ImageButton1" src="../Images/ButtonClose.png" onclick="closewinITA();" style="height:15px;width:15px;" />
            </div>
            <iframe id="IframeITA" style="width: 100%; height: auto; border-style: none;"></iframe>
        </div>

        <div id="divFuhe" style=" position: absolute; top: 15%; left: 35%; width: 350px; height: 240px; background-color: white; border: 1px solid #959595;"
            class="easyui-window" title=" " closed="true" collapsible="false" minimizable="false" maximizable="false" closable="false">
            <div style="text-align: right;">
                <input type="image" name="ImageButton2" id="ImageButton2" src="../Images/ButtonClose.png" onclick="closewinFuhe();" style="height:15px;width:15px;" />
            </div>
            <iframe id="IframeFuhe" style="width: 100%; height: auto; border-style: none;"></iframe>
        </div>
    </form>
</body>
</html>
