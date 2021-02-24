import re



def split_buf(src_buf):
    lines = re.split('[\n\r]', src_buf)
    nest_depth = 0
    cur_struct = ""
    struct_name = ''
    struct_mem_list = []
    for i in lines:
        #print(i)
        if i.find('{') != -1:
            nest_depth = nest_depth + 1
        elif i.find('}') != -1:
            nest_depth = nest_depth - 1
            #待添加代码支持递归定义
            if nest_depth == 0:
                ret = re.match(r'.?\s?(\w*).?;',  i)
                struct_name = ret.group(1)
                #print(struct_name)
        elif nest_depth > 0:
            elem  = {}
            ret = re.search(r'\s*(\w*)\s*(\w*)\s*[:]*\s*(\d*)\s*;', i)
            if ret:
                if ret.group(3):
                    elem['length'] = ret.group(3)
                if ret.group(2):
                    elem['name'] = ret.group(2)
                if ret.group(1):
                    elem['type'] = ret.group(1)
                struct_mem_list.append(elem)
    return  {'mem_list':struct_mem_list,'name':struct_name}

src = '''
typedef struct tag_UE_EUTRA_CAP_V9
{
    U32 featureGroupV9;
    U8 dtm;
    U8 e_RedirectionGERAN_r9;
    U8 e_RedirectionUTRA_r9;
    U8 e_csfb_1xrtt_flag;
    U8 e_csfb_concps_mob1xtrr_r9;
    U8 deviceType;
    U8 intraFreqProxInd_r9;
    U8 interFreqProxInd_r9;
    U8 utran_ProxInd_r9;
    U8 intraFreqSI_AcqForHO_r9;
    U8 interFreqSI_AcqForHO_r9;
    U8 utran_SI_AcqForHO_r9;
    U8 rachReport;
} UE_EUTRA_CAP_V9;
'''

if __name__ == "__main__":
    #matchObj = re.search(r'\s*(\w*)\s*(\w*)\s*[:]*\s*(\d*)\s*;', 'INT32 count : 24 ;', )
    #print(matchObj.group(1))
    #print(matchObj.group(2))
    #print(matchObj.group(3))
    print(split_buf(src))
