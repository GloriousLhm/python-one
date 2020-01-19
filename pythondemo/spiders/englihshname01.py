# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class Englihshname01Spider(scrapy.Spider):
    name = 'englihshname01'
    allowed_domains = ['www.resgain.net']
    start_urls = [
            'http://www.resgain.net/english_names.html',
            "http://www.resgain.net/english_names_2.html",
            "http://www.resgain.net/english_names_2.html",
            "http://www.resgain.net/english_names_3.html",
            "http://www.resgain.net/english_names_4.html",
            "http://www.resgain.net/english_names_5.html",
            "http://www.resgain.net/english_names_6.html",
            "http://www.resgain.net/english_names_7.html",
            "http://www.resgain.net/english_names_8.html",
             "http://www.resgain.net/english_names_9.html",
            "http://www.resgain.net/english_names_10.html",
            "http://www.resgain.net/english_names_11.html",
            "http://www.resgain.net/english_names_12.html",
            "http://www.resgain.net/english_names_13.html",
            "http://www.resgain.net/english_names_14.html",
            "http://www.resgain.net/english_names_15.html",
            "http://www.resgain.net/english_names_16.html",
            "http://www.resgain.net/english_names_17.html",
            "http://www.resgain.net/english_names_18.html",
            "http://www.resgain.net/english_names_19.html",
            "http://www.resgain.net/english_names_20.html",
            "http://www.resgain.net/english_names_21.html",
            "http://www.resgain.net/english_names_22.html",

            'http://www.resgain.net/english_names_b.html',
            "http://www.resgain.net/english_names_b_2.html",
            "http://www.resgain.net/english_names_b_3.html",
            "http://www.resgain.net/english_names_b_4.html",
            "http://www.resgain.net/english_names_b_6.html",
            "http://www.resgain.net/english_names_b_7.html",
            "http://www.resgain.net/english_names_b_8.html",
            "http://www.resgain.net/english_names_b_9.html",
            "http://www.resgain.net/english_names_b_10.html",
            "http://www.resgain.net/english_names_b_11.html",
            "http://www.resgain.net/english_names_b_12.html",
            "http://www.resgain.net/english_names_b_13.html",
            "http://www.resgain.net/english_names_b_14.html",
            "http://www.resgain.net/english_names_b_15.html",

            "http://www.resgain.net/english_names_c.html"
            "http://www.resgain.net/english_names_c_2.html",
            "http://www.resgain.net/english_names_c_3.html",
            "http://www.resgain.net/english_names_c_4.html",
            "http://www.resgain.net/english_names_c_6.html",
            "http://www.resgain.net/english_names_c_7.html",
            "http://www.resgain.net/english_names_c_8.html",
            "http://www.resgain.net/english_names_c_9.html",
            "http://www.resgain.net/english_names_c_10.html",
            "http://www.resgain.net/english_names_c_11.html",
            "http://www.resgain.net/english_names_c_12.html",
            "http://www.resgain.net/english_names_c_13.html",
            "http://www.resgain.net/english_names_c_14.html",
            "http://www.resgain.net/english_names_c_15.html",
            "http://www.resgain.net/english_names_c_16.html"

            "http://www.resgain.net/english_names_d.html"
            "http://www.resgain.net/english_names_d_2.html",
            "http://www.resgain.net/english_names_d_3.html",
            "http://www.resgain.net/english_names_d_4.html",
            "http://www.resgain.net/english_names_d_6.html",
            "http://www.resgain.net/english_names_d_7.html",
            "http://www.resgain.net/english_names_d_8.html",
            "http://www.resgain.net/english_names_d_9.html",
            "http://www.resgain.net/english_names_d_10.html",
            "http://www.resgain.net/english_names_d_11.html",
            "http://www.resgain.net/english_names_d_12.html",
            "http://www.resgain.net/english_names_d_13.html",
            "http://www.resgain.net/english_names_d_14.html",
            "http://www.resgain.net/english_names_d_15.html",
            "http://www.resgain.net/english_names_d_16.html",
            "http://www.resgain.net/english_names_d_17.html"

            "http://www.resgain.net/english_names_e.html"
            "http://www.resgain.net/english_names_e_2.html",
            "http://www.resgain.net/english_names_e_3.html",
            "http://www.resgain.net/english_names_e_4.html",
            "http://www.resgain.net/english_names_e_6.html",
            "http://www.resgain.net/english_names_e_7.html",
            "http://www.resgain.net/english_names_e_8.html",
            "http://www.resgain.net/english_names_e_9.html",
            "http://www.resgain.net/english_names_e_10.html",
            "http://www.resgain.net/english_names_e_11.html",
            "http://www.resgain.net/english_names_e_12.html",
            "http://www.resgain.net/english_names_e_13.html",

            "http://www.resgain.net/english_names_f.html"
            "http://www.resgain.net/english_names_f_2.html",
            "http://www.resgain.net/english_names_f_3.html",
            "http://www.resgain.net/english_names_f_4.html",
            "http://www.resgain.net/english_names_f_6.html",
            "http://www.resgain.net/english_names_f_7.html",
            "http://www.resgain.net/english_names_f_8.html",
            "http://www.resgain.net/english_names_f_9.html",
            "http://www.resgain.net/english_names_f_10.html",
            "http://www.resgain.net/english_names_f_11.html",
            "http://www.resgain.net/english_names_f_12.html",

            "http://www.resgain.net/english_names_g.html"
            "http://www.resgain.net/english_names_g_2.html",
            "http://www.resgain.net/english_names_g_3.html",
            "http://www.resgain.net/english_names_g_4.html",
            "http://www.resgain.net/english_names_g_6.html",
            "http://www.resgain.net/english_names_g_7.html",
            "http://www.resgain.net/english_names_g_8.html",
            "http://www.resgain.net/english_names_g_9.html",
            "http://www.resgain.net/english_names_g_10.html",
            "http://www.resgain.net/english_names_g_11.html",
            "http://www.resgain.net/english_names_g_12.html",
            "http://www.resgain.net/english_names_g_13.html",

            "http://www.resgain.net/english_names_h.html"
            "http://www.resgain.net/english_names_h_2.html",
            "http://www.resgain.net/english_names_h_3.html",
            "http://www.resgain.net/english_names_h_4.html",
            "http://www.resgain.net/english_names_h_6.html",
            "http://www.resgain.net/english_names_h_7.html",
            "http://www.resgain.net/english_names_h_8.html",
            "http://www.resgain.net/english_names_h_9.html",
            "http://www.resgain.net/english_names_h_10.html",
            "http://www.resgain.net/english_names_h_11.html",
            "http://www.resgain.net/english_names_h_12.html",
            "http://www.resgain.net/english_names_h_13.html",

            "http://www.resgain.net/english_names_i.html"
            "http://www.resgain.net/english_names_i_2.html",
            "http://www.resgain.net/english_names_i_3.html",
            "http://www.resgain.net/english_names_i_4.html",
            "http://www.resgain.net/english_names_i_6.html",
            "http://www.resgain.net/english_names_i_7.html",
            "http://www.resgain.net/english_names_i_8.html",
            "http://www.resgain.net/english_names_i_9.html",
            "http://www.resgain.net/english_names_i_10.html",
            "http://www.resgain.net/english_names_i_11.html",

            "http://www.resgain.net/english_names_j.html"
            "http://www.resgain.net/english_names_j_2.html",
            "http://www.resgain.net/english_names_j_3.html",
            "http://www.resgain.net/english_names_j_4.html",
            "http://www.resgain.net/english_names_j_6.html",
            "http://www.resgain.net/english_names_j_7.html",
            "http://www.resgain.net/english_names_j_8.html",
            "http://www.resgain.net/english_names_j_9.html",

            "http://www.resgain.net/english_names_k.html"
            "http://www.resgain.net/english_names_k_2.html",
            "http://www.resgain.net/english_names_k_3.html",
            "http://www.resgain.net/english_names_k_4.html",
            "http://www.resgain.net/english_names_k_6.html",
            "http://www.resgain.net/english_names_k_7.html",
            "http://www.resgain.net/english_names_k_8.html",
            "http://www.resgain.net/english_names_k_9.html",
            "http://www.resgain.net/english_names_k_10.html",
            "http://www.resgain.net/english_names_k_11.html",
            "http://www.resgain.net/english_names_k_12.html",

            "http://www.resgain.net/english_names_l.html"
            "http://www.resgain.net/english_names_l_2.html",
            "http://www.resgain.net/english_names_l_3.html",
            "http://www.resgain.net/english_names_l_4.html",
            "http://www.resgain.net/english_names_l_6.html",
            "http://www.resgain.net/english_names_l_7.html",
            "http://www.resgain.net/english_names_l_8.html",
            "http://www.resgain.net/english_names_l_9.html",
            "http://www.resgain.net/english_names_l_10.html",
            "http://www.resgain.net/english_names_l_11.html",
            "http://www.resgain.net/english_names_l_12.html",
            "http://www.resgain.net/english_names_l_13.html",

            "http://www.resgain.net/english_names_m.html"
            "http://www.resgain.net/english_names_m_2.html",
            "http://www.resgain.net/english_names_m_3.html",
            "http://www.resgain.net/english_names_m_4.html",
            "http://www.resgain.net/english_names_m_6.html",
            "http://www.resgain.net/english_names_m_7.html",
            "http://www.resgain.net/english_names_m_8.html",
            "http://www.resgain.net/english_names_m_9.html",
            "http://www.resgain.net/english_names_m_10.html",
            "http://www.resgain.net/english_names_m_11.html",
            "http://www.resgain.net/english_names_m_12.html",
            "http://www.resgain.net/english_names_m_13.html",
            "http://www.resgain.net/english_names_m_14.html",

            "http://www.resgain.net/english_names_n.html"
            "http://www.resgain.net/english_names_n_2.html",
            "http://www.resgain.net/english_names_n_3.html",
            "http://www.resgain.net/english_names_n_4.html",
            "http://www.resgain.net/english_names_n_6.html",
            "http://www.resgain.net/english_names_n_7.html",
            "http://www.resgain.net/english_names_n_8.html",
            "http://www.resgain.net/english_names_n_9.html",
            "http://www.resgain.net/english_names_n_10.html",
            "http://www.resgain.net/english_names_n_11.html",
            "http://www.resgain.net/english_names_n_12.html",

            "http://www.resgain.net/english_names_o.html"
            "http://www.resgain.net/english_names_o_2.html",
            "http://www.resgain.net/english_names_o_3.html",
            "http://www.resgain.net/english_names_o_4.html",
            "http://www.resgain.net/english_names_o_6.html",
            "http://www.resgain.net/english_names_o_7.html",
            "http://www.resgain.net/english_names_o_8.html",

            "http://www.resgain.net/english_names_p.html"
            "http://www.resgain.net/english_names_p_2.html",
            "http://www.resgain.net/english_names_p_3.html",
            "http://www.resgain.net/english_names_p_4.html",
            "http://www.resgain.net/english_names_p_6.html",
            "http://www.resgain.net/english_names_p_7.html",
            "http://www.resgain.net/english_names_p_8.html",
            "http://www.resgain.net/english_names_p_9.html",
            "http://www.resgain.net/english_names_p_10.html",
            "http://www.resgain.net/english_names_p_11.html",
            "http://www.resgain.net/english_names_p_12.html",

            "http://www.resgain.net/english_names_q.html"
            "http://www.resgain.net/english_names_q_2.html",
            "http://www.resgain.net/english_names_q_3.html",

            "http://www.resgain.net/english_names_r.html"
            "http://www.resgain.net/english_names_r_2.html",
            "http://www.resgain.net/english_names_r_3.html",
            "http://www.resgain.net/english_names_r_4.html",
            "http://www.resgain.net/english_names_r_6.html",
            "http://www.resgain.net/english_names_r_7.html",
            "http://www.resgain.net/english_names_r_8.html",
            "http://www.resgain.net/english_names_r_9.html",
            "http://www.resgain.net/english_names_r_10.html",
            "http://www.resgain.net/english_names_r_11.html",
            "http://www.resgain.net/english_names_r_12.html",

            "http://www.resgain.net/english_names_s.html"
            "http://www.resgain.net/english_names_s_2.html",
            "http://www.resgain.net/english_names_s_3.html",
            "http://www.resgain.net/english_names_s_4.html",
            "http://www.resgain.net/english_names_s_6.html",
            "http://www.resgain.net/english_names_s_7.html",
            "http://www.resgain.net/english_names_s_8.html",
            "http://www.resgain.net/english_names_s_9.html",
            "http://www.resgain.net/english_names_s_10.html",
            "http://www.resgain.net/english_names_s_11.html",

            "http://www.resgain.net/english_names_t.html"
            "http://www.resgain.net/english_names_t_2.html",
            "http://www.resgain.net/english_names_t_3.html",
            "http://www.resgain.net/english_names_t_4.html",
            "http://www.resgain.net/english_names_t_6.html",
            "http://www.resgain.net/english_names_t_7.html",
            "http://www.resgain.net/english_names_t_8.html",
            "http://www.resgain.net/english_names_t_9.html",
            "http://www.resgain.net/english_names_t_10.html",
            "http://www.resgain.net/english_names_t_11.html",
            "http://www.resgain.net/english_names_t_12.html",
            "http://www.resgain.net/english_names_t_13.html",
            "http://www.resgain.net/english_names_t_14.html",

            "http://www.resgain.net/english_names_u.html"
            "http://www.resgain.net/english_names_u_2.html",
            "http://www.resgain.net/english_names_u_3.html",
            "http://www.resgain.net/english_names_u_4.html",

            "http://www.resgain.net/english_names_v.html"
            "http://www.resgain.net/english_names_v_2.html",
            "http://www.resgain.net/english_names_v_3.html",
            "http://www.resgain.net/english_names_v_4.html",
            "http://www.resgain.net/english_names_v_6.html",
            "http://www.resgain.net/english_names_v_7.html",
            "http://www.resgain.net/english_names_v_8.html",
            "http://www.resgain.net/english_names_v_9.html",
            "http://www.resgain.net/english_names_v_10.html",

            "http://www.resgain.net/english_names_w.html"
            "http://www.resgain.net/english_names_w_2.html",
            "http://www.resgain.net/english_names_w_3.html",
            "http://www.resgain.net/english_names_w_4.html",
            "http://www.resgain.net/english_names_w_6.html",
            "http://www.resgain.net/english_names_w_7.html",
            "http://www.resgain.net/english_names_w_8.html",
            "http://www.resgain.net/english_names_w_9.html",

            "http://www.resgain.net/english_names_x.html"
            "http://www.resgain.net/english_names_x_2.html",

            "http://www.resgain.net/english_names_y.html"
            "http://www.resgain.net/english_names_y_2.html",
            "http://www.resgain.net/english_names_y_3.html",
            "http://www.resgain.net/english_names_y_4.html",

            "http://www.resgain.net/english_names_z.html"
            "http://www.resgain.net/english_names_z_2.html",
            "http://www.resgain.net/english_names_z_3.html",
            "http://www.resgain.net/english_names_z_4.html",
            "http://www.resgain.net/english_names_z_6.html",
            "http://www.resgain.net/english_names_z_7.html",
            "http://www.resgain.net/english_names_z_8.html",
            "http://www.resgain.net/english_names_z_9.html",




                  ]

    def parse(self, response):
        namelist = response.xpath("//div/table[@class='table']/tbody/tr")
        for item in namelist:
            print(item)
            # 创建一个变量 item文件导进来
            enname_itme = PythondemoItem()
            enname_itme['firstname']=item.xpath("./td[1]/text()").extract_first()
            #    把数据yield到管道中去
            yield enname_itme

        next_link = response.xpath("//div/ul[@class='pagination']/li[@class='nextpage']/a/@href").extract()
        print(next_link)
        print(999)
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("http://www.resgain.net" + next_link, callback=self.parse)


