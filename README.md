# 5etools自动化翻译项目
> 本项目fork自https://github.com/5etools-translated/5etools-translated.github.io/tree/translations

# 项目修复与更新
- 修复了自动deepl翻译无法捕捉翻译框的错误
- 专注于中文自动化翻译，对中文进行了更好的支持
- 修复了deepl自动翻译时翻译结果不全的问题
- 修复了全角括号造成的变量无法替换问题
- 增加了GPT翻译方式，支持自定义代理地址和自定义模型调用
- 增加环境变量，更新了translate工作流
- 将翻译数据源替换为了第二版的5etools

# 项目进展  
目前绝大部分内容都已经进行了汉化，基本导入fvtt使用都没有问题。   
**注意：** 由于所有内容的名称关联很多，工作量过大，所以名称不在翻译的范围内，未来应该也不会考虑翻译

# 使用方法  
随机打开一个导入页，然后点击右下角设置图标进入设置
<img width="1069" alt="image" src="https://github.com/monthwolf/5etools-zh.github.io/assets/52775320/cfcb00ad-bbb7-434f-b8d7-ac796ddbfa3e">

</br></br>
<img width="815" alt="image" src="https://github.com/monthwolf/5etools-zh.github.io/assets/52775320/09679b4c-c05d-4765-b6e0-14ca016e99be">


根据上图，在Data Sources设置中  
开启`Avoid Loading Local Data`选项  
**【国内】**  
将`Base Site Url`改为: https://raw.gitmirror.com/monthwolf/5etools-zh.github.io/main/  
将`Base Homebrew Repository Url`改为: https://raw.gitmirror.com/monthwolf/homebrew-translated/zh/data.zh/  
将`Base Prerelease Repository Url`改为: https://raw.gitmirror.com/TheGiddyLimit/unearthed-arcana/master/  


备用链接1：  
将`Base Site Url`改为: https://mirror.ghproxy.com/https://raw.githubusercontent.com/monthwolf/5etools-zh.github.io/main/     
将`Base Homebrew Repository Url`改为: https://mirror.ghproxy.com/https://raw.githubusercontent.com/monthwolf/homebrew-translated/zh/data.zh/  
将`Base Prerelease Repository Url`改为: https://mirror.ghproxy.com/https://raw.githubusercontent.com/TheGiddyLimit/unearthed-arcana/master/  
备用链接2:
将`Base Site Url`改为: https://cdn.jsdelivr.net/gh/monthwolf/5etools-zh.github.io@main/    
将`Base Homebrew Repository Url`改为: https://cdn.jsdelivr.net/gh/monthwolf/homebrew-translated@zh/data.zh/  
将`Base Prerelease Repository Url`改为: https://cdn.jsdelivr.net/gh/TheGiddyLimit/unearthed-arcana@master/  

**【无法使用】**
对于以上两种链接都无法使用的情况，请直接打包data文件夹，然后覆盖替换mod文件夹中plutonium中的data文件夹（建议做好备份）   
还原Data Sources设置，取消勾选`Avoid Loading Local Data`选项，留空`Base Site Url`、`Base Homebrew Repository Url`、`Base Prerelease Repository Url`  
> data文件夹打包方式:可使用[DownGit](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/monthwolf/5etools-zh.github.io/tree/main/data.zh)打包

**【国外】**
将`Base Site Url`改为: https://raw.githubusercontent.com/monthwolf/5etools-zh.github.io/main/ 或 https://monthwolf.github.io/5etools-zh.github.io/ 
将`Base Homebrew Repository Url`改为: https://raw.githubusercontent.com/monthwolf/homebrew-translated/zh/data.zh/

# 展示
<img width="1280" alt="image" src="https://github.com/monthwolf/5etools-zh.github.io/assets/52775320/6ddf1016-bd51-48f0-a8a3-9402e28bab03">
<img width="1280" alt="image" src="https://github.com/monthwolf/5etools-zh.github.io/assets/52775320/104c4395-9a38-4d7b-b588-cf96b6b40c22">
<img width="1280" alt="image" src="https://github.com/monthwolf/5etools-zh.github.io/assets/52775320/cd32c02e-578b-4a4d-b975-af3d06533402">
