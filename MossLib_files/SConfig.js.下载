let config = {
	jumpFileParseByBrowserTab:true,//是否通过浏览器页签 智问跳转智读  true是 false页签打开
	
	isUploadAr:true,//是否上传阿语 ，需要单独解析
	

	isVisibleDMSEquipment:true,//是否显示智库-装备库信息
	dmsSystemBaseUrl:"http://yr2501209d.dms365.com.cn/",//达美盛-装备库查看详情基于地址
	
	knowledgeAskUploadFileCount:1,//智问上传文件个数 1个
	uploadExceedLimitSizeM:100,//智问上传文件大小 100M  （智问、智读、Ai文档翻译）
	uploadLimitsForKnowledgeAsk:[
		{label:"Word支持的文件格式：",langCode:"wordFormats",fileType:"docx,doc"},
		{label:"Pdf支持的文件格式：",langCode:"pdfFormats",fileType:"pdf"},
		{label:"Txt支持的文件格式：",langCode:"txtFormats",fileType:"txt"},
	],
	
	/* systemInfo:{
		showLogoTitle:true,//是否显示title
		logoTitle:"准 意",
		logoUrl:"/systemImg/logo.png",
		logoUrlIco:"/systemImg/logo.ico",
		kbAskDefaultImg:"/systemImg/ai-search-tools.png"//智问的初始页面背景图
	}, */

	systemInfo:{
		showLogoTitle:false,//是否显示title
		logoTitle:"MossLib",
		logoUrl:"/systemImg/logo_mosslib.png",
		// logoUrlLong:"/systemImg/logo_mosslib_long.png",//有logoTitle时， 不显示长logo
		logoUrlLong:"/systemImg/logo_mosslib_long_v2.3.png",//有logoTitle时， 不显示长logo
		logoUrlIco:"/systemImg/logo_mosslib.ico",
		kbAskDefaultImg:"/systemImg/ai-search-tools-newtranx.png",//智问的初始页面背景图
		
		retrieveDefaultImg:"/systemImg/logo_mosslib_long.png",//mosslibV2 首页默认图
	},
	
	// testPrefixBaseUrl:"http://mosslib-test.newtranx.com/prod-api",//临时访问测试检索数据，报告类型文件的前缀
	// testPrefixNotBaseUrl:"/mosslib-prod-api",
	
	sameTimeHandleMaxCount_aiChat:1,//智读上传文件数量
	//AI智读 上传格式限制
	uploadLimitsForAiChat:"docx、pdf",//doc、
	uploadLimitsForLib:"pdf",//doc、
		
	sameTimeHandleMaxCount_aiTransDoc:1,//Ai文档翻译上传文件数量
	//uploadLimitsForAiChat:"docx、pdf",//Ai文档翻译上传格式
	uploadLimitsForAiTransDoc:"pdf",//Ai文档翻译上传格式	

	
	uploadImgLimitSizeMForAiWrite:5,//上传图片大小限制 5M
	uploadImgLimitsForAiWrite:[
		{label:"png格式：",langCode:"pngFormats",fileType:"png"},
		{label:"jpg格式：",langCode:"jpgFormats",fileType:"jpg,jpeg"},
	],
	
	uploadLimitsForAiWrite:"docx",
	uploadExceedLimitSizeMForAiWrite:10,//10M
	exportTypeForAiWrite:'local',//智写导出方式  local自定义接口，online在线联网接口
	
	clueContentMaxLimit:5000,//单条线索内容 最长字符串长度  默认5000
	
	// 文档翻译 - AI助手 指令配置
	chatInstructListV2:[{
		label:"问答",
		value:"question-answer",
		icon:"instruct-question-answer",
		template:{//type_1 默认设置区指令操作 ；  type_2 引用-非问答 ； //type_3 引用-问答-切换其他指令
			type_1:{
				placeholder:"向当前文档提问",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`回答这个问题：“[txt]”`,
				//instructRule:`使用[lang]回答这个问题：“[txt]”`,
				askBaseMsg:`[txt]`,
				askQuoteMsg:"",
			},
			type_2:{//引用-问答 
				placeholder:"问我关于引用内容的任何问题",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`参考以下文本“[quoteTxt]”，回答这个问题：“[txt]”`,
				//instructRule:`参考以下文本“[quoteTxt]”，使用[lang]回答这个问题：“[txt]”`,
				askBaseMsg:`[txt]`,
				askQuoteMsg:`[quoteTxt]`,
			}
		}
	}],
	
	//AI智读 指令配置
	chatInstructList:[{
		label:"问答",
		value:"question-answer",
		icon:"instruct-question-answer",
		template:{//type_1 默认设置区指令操作 ；  type_2 引用-非问答 ； //type_3 引用-问答-切换其他指令
			type_1:{
				placeholder:"问我任何问题",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`回答这个问题：“[txt]”`,
				//instructRule:`使用[lang]回答这个问题：“[txt]”`,
				askBaseMsg:`[txt]`,
				askQuoteMsg:"",
			},
			type_2:{//引用-问答 
				placeholder:"问我关于引用内容的任何问题",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`参考以下文本“[quoteTxt]”，回答这个问题：“[txt]”`,
				//instructRule:`参考以下文本“[quoteTxt]”，使用[lang]回答这个问题：“[txt]”`,
				askBaseMsg:`[txt]`,
				askQuoteMsg:`[quoteTxt]`,
			}
		}
	},{
		label:"翻译",
		value:"translate",
		icon:"instruct-translate",
		template:{//type_1 默认设置区指令操作 ；  type_2 引用-非问答 ； //type_3 引用-问答-切换其他指令
			type_1:{
				iptTopMsg:"翻译为[lang]",//240906 未输入文本时 显示在输入上方的内容
				placeholder:"请输入要翻译的原文",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`将以下文本翻译为[lang]：“[txt]”`,
				askBaseMsg:`请将以下文字翻译为[lang]：`,
				askQuoteMsg:`[txt]`,
			},
			type_2:{//引用-非问答
				placeholder:"",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`将以下文本翻译为[lang]：“[quoteTxt]”`,
				askBaseMsg:`请将以下文字翻译为[lang]：`,
				askQuoteMsg:`[quoteTxt]`,
			},
			/*type_3:{//引用-问答-切换其他指令
				placeholder:"请输入要翻译的原文",//输入框内容
				defaultIptTxt:"翻译引用内容",//默认输入框文本
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`将以下文本翻译为[lang]：“[quoteTxt]”+“，”+[txt]`,
				askBaseMsg:`请将以下文本翻译为[lang]，[txt]：`,
				askQuoteMsg:`[quoteTxt]`,
			}*/
		}
	},
	// {
	// 	label:"改写",
	// 	value:"rewrite",
	// 	icon:"instruct-rewrite",
	// 	template:{//type_1 默认设置区指令操作 ；  type_2 引用-非问答 ； //type_3 引用-问答-切换其他指令
	// 		type_1:{
	// 			placeholder:"请输入要改写的原文",//输入框内容
	// 			showAskType:true,//发送消息 是否显示 问答类型
	// 			instructRule:`用[lang]改写以下文字：“[txt]”`,
	// 			askBaseMsg:`请用[lang]改写以下文字：`,
	// 			askQuoteMsg:`[txt]`,
	// 		},
	// 		type_2:{//引用-非问答
	// 			placeholder:"",//输入框内容
	// 			showAskType:true,//发送消息 是否显示 问答类型
	// 			instructRule:`用[lang]改写以下文字：“[quoteTxt]”`,
	// 			askBaseMsg:`请用[lang]改写以下文字：`,
	// 			askQuoteMsg:`[quoteTxt]`,
	// 		},
	// 		/*type_3:{//引用-问答-切换其他指令
	// 			placeholder:"输入要改写的原文",//输入框内容
	// 			defaultIptTxt:"输入要改写的原文",//默认输入框文本
	// 			showAskType:true,//发送消息 是否显示 问答类型
	// 			instructRule:`用[lang]改写以下文字：“[quoteTxt]”+“，”+[txt]`,
	// 			askBaseMsg:`使用[lang]，[txt]：`,
	// 			askQuoteMsg:`[quoteTxt]`,
	// 		}*/
	// 	}
	// },
	{
		label:"总结",
		value:"summarize",
		icon:"instruct-summarize",
		template:{//type_1 默认设置区指令操作 ；  type_2 引用-非问答 ； //type_3 引用-问答-切换其他指令
			type_1:{
				iptTopMsg:"总结",//240906 未输入文本时 显示在输入上方的内容
				placeholder:"请输入要总结的原文",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`总结这段话“[txt]”`,
				askBaseMsg:`总结以下内容：`,
				// instructRule:`使用[lang]总结这段话“[txt]”`,
				// askBaseMsg:`请用[lang]总结以下内容：`,
				askQuoteMsg:`[txt]`,
			},
			type_2:{//引用-非问答
				placeholder:"",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`总结这段话“[quoteTxt]”`,
				askBaseMsg:`总结以下内容：`,
				// instructRule:`使用[lang]总结这段话“[quoteTxt]”`,
				// askBaseMsg:`请用[lang]总结以下内容：`,
				askQuoteMsg:`[quoteTxt]`,
			},
			/*type_3:{//引用-问答-切换其他指令
				placeholder:"请输入要总结的原文",//输入框内容
				defaultIptTxt:"对引用内容进行总结",//默认输入框文本
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`使用[lang]总结这段话“[quoteTxt]”+“，”+[txt]`,
				askBaseMsg:`使用[lang]，[txt]：`,
				askQuoteMsg:`[quoteTxt]`,
			}*/
		}
	},{
		label:"解释",
		value:"explain",
		icon:"instruct-explain",
		template:{//type_1 默认设置区指令操作 ；  type_2 引用-非问答 ； //type_3 引用-问答-切换其他指令
			type_1:{
				iptTopMsg:"解释",//240906 未输入文本时 显示在输入上方的内容
				placeholder:"请输入要解释的内容",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`解释以下文字：“[txt]”`,
				askBaseMsg:`解释以下文字：`,
				// instructRule:`用[lang]解释以下文字：“[txt]”`,
				// askBaseMsg:`请用[lang]解释以下文字：`,
				askQuoteMsg:`[txt]`,
			},
			type_2:{//引用-非问答
				placeholder:"",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`解释以下文字：“[quoteTxt]”`,
				askBaseMsg:`解释以下文字：`,
				// instructRule:`用[lang]解释以下文字：“[quoteTxt]”`,
				// askBaseMsg:`请用[lang]解释以下文字：`,
				askQuoteMsg:`[quoteTxt]`,
			},
			/*type_3:{//引用-问答-切换其他指令
				placeholder:"请输入要解释的内容",//输入框内容
				defaultIptTxt:"对引用内容进行解释",//默认输入框文本
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`用[lang]解释以下文字：“[quoteTxt]”+“，”+[txt]`,
				askBaseMsg:`使用[lang]，[txt]：`,
				askQuoteMsg:`[quoteTxt]`,
			}*/
		}
	},{
		label:"润色",//新增的指令 
		value:"polish",
		icon:"instruct-polish",
		template:{//type_1 默认设置区指令操作 ；  type_2 引用-非问答 ； //type_3 引用-问答-切换其他指令
			type_1:{
				iptTopMsg:"润色",//240906 未输入文本时 显示在输入上方的内容
				placeholder:"请输入要润色的内容",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`润色以下文字：“[txt]”`,
				askBaseMsg:`润色以下文字：`,
				// instructRule:`用[lang]润色以下文字：“[txt]”`,
				// askBaseMsg:`请用[lang]润色以下文字：`,
				askQuoteMsg:`[txt]`,
			},
			type_2:{//引用-非问答
				placeholder:"",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`润色以下文字：“[quoteTxt]”`,
				askBaseMsg:`润色以下文字：`,
				// instructRule:`用[lang]润色以下文字：“[quoteTxt]”`,
				// askBaseMsg:`请用[lang]润色以下文字：`,
				askQuoteMsg:`[quoteTxt]`,
			},
			/*type_3:{//引用-问答-切换其他指令
				placeholder:"请输入要解释的内容",//输入框内容
				defaultIptTxt:"对引用内容进行解释",//默认输入框文本
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`用[lang]解释以下文字：“[quoteTxt]”+“，”+[txt]`,
				askBaseMsg:`使用[lang]，[txt]：`,
				askQuoteMsg:`[quoteTxt]`,
			}*/
		}
	},{
		label:"续写",
		value:"continuation",
		icon:"instruct-continuation",
		template:{//type_1 默认设置区指令操作 ；  type_2 引用-非问答 ； //type_3 引用-问答-切换其他指令
			type_1:{
				iptTopMsg:"续写",//240906 未输入文本时 显示在输入上方的内容
				placeholder:"请输入要续写的原文",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`续写以下文字：“[txt]”`,
				askBaseMsg:`续写以下文字：`,
				// instructRule:`用[lang]续写以下文字：“[txt]”`,
				// askBaseMsg:`请用[lang]续写以下文字：`,
				askQuoteMsg:`[txt]`,
			},
			type_2:{//引用-非问答
				placeholder:"",//输入框内容
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`续写以下文字：“[quoteTxt]”`,
				askBaseMsg:`续写以下文字：`,
				// instructRule:`用[lang]续写以下文字：“[quoteTxt]”`,
				// askBaseMsg:`请用[lang]续写以下文字：`,
				askQuoteMsg:`[quoteTxt]`,
			},
			/*type_3:{//引用-问答-切换其他指令
				placeholder:"请输入要续写的原文",//输入框内容
				defaultIptTxt:"对引用内容进行续写",//默认输入框文本
				showAskType:true,//发送消息 是否显示 问答类型
				instructRule:`用[lang]续写以下文字：“[quoteTxt]”+“，”+[txt]`,
				askBaseMsg:`使用[lang]，[txt]：`,
				askQuoteMsg:`[quoteTxt]`,
			}*/
		}
	}]
}