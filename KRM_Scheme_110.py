#Загрузка PP в Python
import pandapower as pp

#Создание пустой сети
net = pp.create_empty_network (f_hz = 50, add_stdtypes = True)

#Создание шин
b1 = pp.create_bus(net, vn_kv = 230, name = 'Система')
b21 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b31 = pp.create_bus(net, vn_kv = 110, name = 'Нагрузка')
b32 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b41 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b62 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b71 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b641 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b631 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b651 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b661 = pp.create_bus(net, vn_kv = 10, name = 'Нагрузка')
b671 = pp.create_bus(net, vn_kv = 10, name = 'ТВС-63-2УЗ')
b51 = pp.create_bus(net, vn_kv = 10, name = 'ТВФ-63-2УЗ')
b52 = pp.create_bus(net, vn_kv = 10, name = 'ТВФ-63-2УЗ')
b2 = pp.create_bus(net, vn_kv = 220, name = '1 шина перед АТР')
b3 = pp.create_bus(net, vn_kv = 220, name = '2 шина перед АТР')
b4 = pp.create_bus(net, vn_kv = 220, name = '1 РУ 220')
b5 = pp.create_bus(net, vn_kv = 220, name = '2 РУ 220')
b6 = pp.create_bus(net, vn_kv = 220, name = '3 РУ 220')
b7 = pp.create_bus(net, vn_kv = 220, name = '4 РУ 220')
b61 = pp.create_bus(net, vn_kv = 110, name = '1 РУ 110')
b64 = pp.create_bus(net, vn_kv = 110, name = '2 РУ 110')
b72 = pp.create_bus(net, vn_kv = 110, name = '3 РУ 110')
b63 = pp.create_bus(net, vn_kv = 110, name = '4 РУ 110')
b65 = pp.create_bus(net, vn_kv = 110, name = '5 РУ 110')
b66 = pp.create_bus(net, vn_kv = 110, name = '6 РУ 110')
b67 = pp.create_bus(net, vn_kv = 110, name = '7 РУ 110')

#Создание ШБМ
pp.create_ext_grid(net, bus = b1, vm_pu = 1, name = 'ШБМ')

#Создание генераторов
G1 = pp.create_gen(net, bus = b671, p_mw = 32, max_q_mvar = 16.1, vm_pu = 1.05, name = 'ТВС-32УЗ')
G2 = pp.create_gen(net, bus = b51, p_mw = 63, max_q_mvar = 30.5, vm_pu = 1.05, name = 'ТВФ-63-2УЗ')
G3 = pp.create_gen(net, bus = b52, p_mw = 63, max_q_mvar = 30.5, vm_pu = 1.05, name = 'ТВФ-63-2УЗ')

#Создание нагрузки
N1 = pp.create_load(net, bus = b21, p_mw = 45, q_mvar = 20, name = 'Нагрузка')
N2 = pp.create_load(net, bus = b31, p_mw = 85, q_mvar = 35, name = 'Нагрузка')
N3 = pp.create_load(net, bus = b32, p_mw = 15, q_mvar = 8, name = 'Нагрузка')
N4 = pp.create_load(net, bus = b41, p_mw = 60, q_mvar = 25, name = 'Нагрузка')
N5 = pp.create_load(net, bus = b62, p_mw = 10, q_mvar = 6, name = 'Нагрузка')
N6 = pp.create_load(net, bus = b71, p_mw = 12, q_mvar = 8, name = 'Нагрузка')
N7 = pp.create_load(net, bus = b641, p_mw = 28, q_mvar = 18, name = 'Нагрузка')
N8 = pp.create_load(net, bus = b631, p_mw = 30, q_mvar = 15, name = 'Нагрузка')
N9 = pp.create_load(net, bus = b651, p_mw = 25, q_mvar = 16, name = 'Нагрузка')
N10 = pp.create_load(net, bus = b661, p_mw = 35, q_mvar = 20, name = 'Нагрузка')


#Создание трансформаторов
T1 = pp.create_transformer_from_parameters(net, hv_bus = b2, lv_bus = b21, sn_mva = 40,
vn_hv_kv = 220, vn_lv_kv = 10, vkr_percent = 0.43, vk_percent = 12, pfe_kw = 50, i0_percent = 0.125, name = 'ТРДН-40000/220')
T2 = pp.create_transformer_from_parameters(net, hv_bus = b2, lv_bus = b21, sn_mva = 40,
vn_hv_kv = 220, vn_lv_kv = 10, vkr_percent = 0.43, vk_percent = 12, pfe_kw = 50, i0_percent = 0.125, name = 'ТРДН-40000/220')
T3 = pp.create_transformer_from_parameters(net, hv_bus = b4, lv_bus = b41, sn_mva = 63,
vn_hv_kv = 220, vn_lv_kv = 10, vkr_percent = 0.4, vk_percent = 11.5, pfe_kw = 70, i0_percent = 0.1, name = 'ТРДЦН-63000/220')
T4 = pp.create_transformer_from_parameters(net, hv_bus = b4, lv_bus = b41, sn_mva = 63,
vn_hv_kv = 220, vn_lv_kv = 10, vkr_percent = 0.4, vk_percent = 11.5, pfe_kw = 70, i0_percent = 0.1, name = 'ТРДЦН-63000/220')
T5 = pp.create_transformer_from_parameters(net, hv_bus = b5, lv_bus = b51, sn_mva = 125,
vn_hv_kv = 220, vn_lv_kv = 10, vkr_percent = 0.3, vk_percent = 11, pfe_kw = 120, i0_percent = 0.1, name = 'ТДЦ-125000/220')
T6 = pp.create_transformer_from_parameters(net, hv_bus = b5, lv_bus = b52, sn_mva = 125,
vn_hv_kv = 220, vn_lv_kv = 10, vkr_percent = 0.3, vk_percent = 11, pfe_kw = 120, i0_percent = 0.1, name = 'ТДЦ-125000/220')
T7 = pp.create_transformer3w_from_parameters(net, hv_bus = b3, mv_bus = b31, lv_bus = b32, name = 'АТДЦТН-125000/220',
                                             sn_hv_mva = 125, sn_mv_mva = 63, sn_lv_mva = 63, vn_hv_kv = 220, vn_mv_kv = 110, vn_lv_kv = 10,
                                             vk_hv_percent = 11,vk_mv_percent = 45, vk_lv_percent = 28, vkr_hv_percent = 0.3, vkr_mv_percent = 0.6,
                                             vkr_lv_percent = 0.6, pfe_kw = 65, i0_percent = 0.4)
T8 = pp.create_transformer3w_from_parameters(net, hv_bus = b3, mv_bus = b31, lv_bus = b32, name = 'АТДЦТН-125000/220',
                                             sn_hv_mva = 125, sn_mv_mva = 63, sn_lv_mva = 63, vn_hv_kv = 220, vn_mv_kv = 110, vn_lv_kv = 10,
                                             vk_hv_percent = 11,vk_mv_percent = 45, vk_lv_percent = 28,
                                             vkr_hv_percent = 0.3,vkr_mv_percent = 0.6, vkr_lv_percent = 0.6, pfe_kw = 65, i0_percent = 0.4)
T9 = pp.create_transformer3w_from_parameters(net, hv_bus = b6, mv_bus = b61, lv_bus = b62, name = 'АТДЦТН-125000/220',
                                             sn_hv_mva = 125, sn_mv_mva = 63, sn_lv_mva = 63, vn_hv_kv = 220, vn_mv_kv = 110, vn_lv_kv = 10,
                                             vk_hv_percent = 11,vk_mv_percent = 45, vk_lv_percent = 28,
                                             vkr_hv_percent = 0.3,vkr_mv_percent = 0.6, vkr_lv_percent = 0.6, pfe_kw = 65, i0_percent = 0.4)
T10 = pp.create_transformer3w_from_parameters(net, hv_bus = b6, mv_bus = b61, lv_bus = b62, name = 'АТДЦТН-125000/220',
                                             sn_hv_mva = 125, sn_mv_mva = 63, sn_lv_mva = 63, vn_hv_kv = 220, vn_mv_kv = 110, vn_lv_kv = 10,
                                             vk_hv_percent = 11,vk_mv_percent = 45, vk_lv_percent = 28,
                                             vkr_hv_percent = 0.3,vkr_mv_percent = 0.6, vkr_lv_percent = 0.6, pfe_kw = 65, i0_percent = 0.4)
T11 = pp.create_transformer3w_from_parameters(net, hv_bus = b7, mv_bus = b71, lv_bus = b72, name = 'АТДЦТН-200000/220',
                                             sn_hv_mva = 200, sn_mv_mva = 100, sn_lv_mva = 100, vn_hv_kv = 220, vn_mv_kv = 110, vn_lv_kv = 10,
                                             vk_hv_percent = 10.5,vk_mv_percent = 38, vk_lv_percent = 25,
                                             vkr_hv_percent = 0.33,vkr_mv_percent = 0.66, vkr_lv_percent = 0.66, pfe_kw = 155, i0_percent = 0.45)
T12 = pp.create_transformer_from_parameters(net, hv_bus = b64, lv_bus = b641, sn_mva = 40,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.43, vk_percent = 10.5, pfe_kw = 34, i0_percent = 0.09, name = 'ТРДН-40000/110')
T13 = pp.create_transformer_from_parameters(net, hv_bus = b64, lv_bus = b641, sn_mva = 40,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.43, vk_percent = 10.5, pfe_kw = 34, i0_percent = 0.09, name = 'ТРДН-40000/110')
T14 = pp.create_transformer_from_parameters(net, hv_bus = b63, lv_bus = b631, sn_mva = 25,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.48, vk_percent = 10.5, pfe_kw = 25, i0_percent = 0.1, name = 'ТРДН-25000/110')
T15 = pp.create_transformer_from_parameters(net, hv_bus = b63, lv_bus = b631, sn_mva = 25,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.48, vk_percent = 10.5, pfe_kw = 25, i0_percent = 0.1, name = 'ТРДН-25000/110')
T16 = pp.create_transformer_from_parameters(net, hv_bus = b65, lv_bus = b651, sn_mva = 25,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.48, vk_percent = 10.5, pfe_kw = 25, i0_percent = 0.1, name = 'ТРДН-25000/110')
T17 = pp.create_transformer_from_parameters(net, hv_bus = b65, lv_bus = b651, sn_mva = 25,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.48, vk_percent = 10.5, pfe_kw = 25, i0_percent = 0.1, name = 'ТРДН-25000/110')
T18 = pp.create_transformer_from_parameters(net, hv_bus = b66, lv_bus = b661, sn_mva = 32,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.4, vk_percent = 10.5, pfe_kw = 25, i0_percent = 0.08, name = 'ТРДН-32000/110')
T19 = pp.create_transformer_from_parameters(net, hv_bus = b66, lv_bus = b661, sn_mva = 32,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.4, vk_percent = 10.5, pfe_kw = 25, i0_percent = 0.08, name = 'ТРДН-32000/110')
T20 = pp.create_transformer_from_parameters(net, hv_bus = b67, lv_bus = b671, sn_mva = 40,
vn_hv_kv = 110, vn_lv_kv = 10, vkr_percent = 0.3, vk_percent = 10.5, pfe_kw = 25, i0_percent = 0.06, name = 'ТД-40000/110')

#Создание электрических линий
l1 = pp.create_line_from_parameters(net, from_bus = b1, to_bus = b2, length_km = 50,
 r_ohm_per_km = 0.075, x_ohm_per_km = 0.42, max_i_ka = 0.572, c_nf_per_km = 0)
l2 = pp.create_line_from_parameters(net, from_bus = b1, to_bus = b3, length_km = 45,
 r_ohm_per_km = 0.075, x_ohm_per_km = 0.42, max_i_ka = 0.572, c_nf_per_km = 0, in_service = False)
l3 = pp.create_line_from_parameters(net, from_bus = b2, to_bus = b3, length_km = 40,
 r_ohm_per_km = 0.098, x_ohm_per_km = 0.429, max_i_ka = 0.309, c_nf_per_km = 0)
l4 = pp.create_line_from_parameters(net, from_bus = b2, to_bus = b4, length_km = 60,
 r_ohm_per_km = 0.098, x_ohm_per_km = 0.429, max_i_ka = 0.071, c_nf_per_km = 0)
l5 = pp.create_line_from_parameters(net, from_bus = b2, to_bus = b4, length_km = 60,
 r_ohm_per_km = 0.098, x_ohm_per_km = 0.429, max_i_ka = 0.071, c_nf_per_km = 0)
l6 = pp.create_line_from_parameters(net, from_bus = b4, to_bus = b5, length_km = 45,
 r_ohm_per_km = 0.098, x_ohm_per_km = 0.429, max_i_ka = 0.121, c_nf_per_km = 0)
l7 = pp.create_line_from_parameters(net, from_bus = b4, to_bus = b5, length_km = 45,
 r_ohm_per_km = 0.098, x_ohm_per_km = 0.429, max_i_ka = 0.121, c_nf_per_km = 0)
l8 = pp.create_line_from_parameters(net, from_bus = b4, to_bus = b6, length_km = 45,
 r_ohm_per_km = 0.121, x_ohm_per_km = 0.435, max_i_ka = 0.097, c_nf_per_km = 0)
l9 = pp.create_line_from_parameters(net, from_bus = b4, to_bus = b6, length_km = 45,
 r_ohm_per_km = 0.121, x_ohm_per_km = 0.435, max_i_ka = 0.097, c_nf_per_km = 0)
l10 = pp.create_line_from_parameters(net, from_bus = b4, to_bus = b7, length_km = 50,
 r_ohm_per_km = 0.098, x_ohm_per_km = 0.429, max_i_ka = 0.018, c_nf_per_km = 0)
l11 = pp.create_line_from_parameters(net, from_bus = b5, to_bus = b7, length_km = 60,
 r_ohm_per_km = 0.075, x_ohm_per_km = 0.42, max_i_ka = 0.109, c_nf_per_km = 0)
l12 = pp.create_line_from_parameters(net, from_bus = b61, to_bus = b64, length_km = 48,
 r_ohm_per_km = 0.162, x_ohm_per_km = 0.413, max_i_ka = 0.022, c_nf_per_km = 0)
l13 = pp.create_line_from_parameters(net, from_bus = b61, to_bus = b64, length_km = 48,
 r_ohm_per_km = 0.162, x_ohm_per_km = 0.413, max_i_ka = 0.022, c_nf_per_km = 0)
l14 = pp.create_line_from_parameters(net, from_bus = b61, to_bus = b63, length_km = 40,
 r_ohm_per_km = 0.121, x_ohm_per_km = 0.435, max_i_ka = 0.079, c_nf_per_km = 0)
l15 = pp.create_line_from_parameters(net, from_bus = b61, to_bus = b63, length_km = 40,
 r_ohm_per_km = 0.121, x_ohm_per_km = 0.435, max_i_ka = 0.079, c_nf_per_km = 0)
l16 = pp.create_line_from_parameters(net, from_bus = b72, to_bus = b65, length_km = 40,
 r_ohm_per_km = 0.249, x_ohm_per_km = 0.427, max_i_ka = 0.086, c_nf_per_km = 0)
l17 = pp.create_line_from_parameters(net, from_bus = b72, to_bus = b65, length_km = 40,
 r_ohm_per_km = 0.249, x_ohm_per_km = 0.427, max_i_ka = 0.086, c_nf_per_km = 0)
l18 = pp.create_line_from_parameters(net, from_bus = b64, to_bus = b66, length_km = 30,
 r_ohm_per_km = 0.249, x_ohm_per_km = 0.427, max_i_ka = 0.01, c_nf_per_km = 0)
l19 = pp.create_line_from_parameters(net, from_bus = b65, to_bus = b66, length_km = 40,
 r_ohm_per_km = 0.162, x_ohm_per_km = 0.413, max_i_ka = 0.05, c_nf_per_km = 0)
l20 = pp.create_line_from_parameters(net, from_bus = b66, to_bus = b67, length_km = 25,
 r_ohm_per_km = 0.249, x_ohm_per_km = 0.427, max_i_ka = 0.086, c_nf_per_km = 0)
l21 = pp.create_line_from_parameters(net, from_bus = b66, to_bus = b67, length_km = 25,
 r_ohm_per_km = 0.249, x_ohm_per_km = 0.427, max_i_ka = 0.086, c_nf_per_km = 0)

pp.diagnostic(net)

#Запуск потока мощности
#pp.runpp(net)

#print(net.res_line)
#print(net.res_bus)
#print(net.res_trafo)