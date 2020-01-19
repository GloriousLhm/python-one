# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem


class Beauty03Spider(scrapy.Spider):
    name = 'beauty03'
    allowed_domains = ['www.shu800.com']
    start_urls = [
        'http://www.shu800.com/xinggan/',
        'http://www.shu800.com/xinggan/index_2.html',
        'http://www.shu800.com/xinggan/index_3.html',
        'http://www.shu800.com/xinggan/index_4.html',
        'http://www.shu800.com/xinggan/index_5.html',
        'http://www.shu800.com/xinggan/index_6.html',
        'http://www.shu800.com/xinggan/index_7.html',
        'http://www.shu800.com/xinggan/index_8.html',
        'http://www.shu800.com/xinggan/index_9.html',
        'http://www.shu800.com/xinggan/index_10.html',
        'http://www.shu800.com/xinggan/index_11.html',
        'http://www.shu800.com/xinggan/index_12.html',
        'http://www.shu800.com/xinggan/index_13.html',
        'http://www.shu800.com/xinggan/index_14.html',
        'http://www.shu800.com/xinggan/index_15.html',
        'http://www.shu800.com/xinggan/index_16.html',
        'http://www.shu800.com/xinggan/index_17.html',
        'http://www.shu800.com/xinggan/index_18.html',
        'http://www.shu800.com/xinggan/index_19.html',

        'http://www.shu800.com/xinggan/index_20.html',
        'http://www.shu800.com/xinggan/index_21.html',
        'http://www.shu800.com/xinggan/index_22.html',
        'http://www.shu800.com/xinggan/index_23.html',
        'http://www.shu800.com/xinggan/index_24.html',
        'http://www.shu800.com/xinggan/index_25.html',
        'http://www.shu800.com/xinggan/index_26.html',
        'http://www.shu800.com/xinggan/index_27.html',
        'http://www.shu800.com/xinggan/index_28.html',
        'http://www.shu800.com/xinggan/index_29.html',

        'http://www.shu800.com/xinggan/index_30.html',
        'http://www.shu800.com/xinggan/index_31.html',
        'http://www.shu800.com/xinggan/index_32.html',
        'http://www.shu800.com/xinggan/index_33.html',
        'http://www.shu800.com/xinggan/index_34.html',
        'http://www.shu800.com/xinggan/index_35.html',
        'http://www.shu800.com/xinggan/index_36.html',
        'http://www.shu800.com/xinggan/index_37.html',
        'http://www.shu800.com/xinggan/index_38.html',
        'http://www.shu800.com/xinggan/index_39.html',

        'http://www.shu800.com/xinggan/index_40.html',
        'http://www.shu800.com/xinggan/index_41.html',
        'http://www.shu800.com/xinggan/index_42.html',
        'http://www.shu800.com/xinggan/index_43.html',
        'http://www.shu800.com/xinggan/index_44.html',
        'http://www.shu800.com/xinggan/index_45.html',
        'http://www.shu800.com/xinggan/index_46.html',
        'http://www.shu800.com/xinggan/index_47.html',
        'http://www.shu800.com/xinggan/index_48.html',
        'http://www.shu800.com/xinggan/index_49.html',

        'http://www.shu800.com/xinggan/index_50.html',
        'http://www.shu800.com/xinggan/index_51.html',
        'http://www.shu800.com/xinggan/index_52.html',
        'http://www.shu800.com/xinggan/index_53.html',
        'http://www.shu800.com/xinggan/index_54.html',
        'http://www.shu800.com/xinggan/index_55.html',
        'http://www.shu800.com/xinggan/index_56.html',
        'http://www.shu800.com/xinggan/index_57.html',
        'http://www.shu800.com/xinggan/index_58.html',
        'http://www.shu800.com/xinggan/index_59.html',

        'http://www.shu800.com/xinggan/index_60.html',
        'http://www.shu800.com/xinggan/index_61.html',
        'http://www.shu800.com/xinggan/index_62.html',
        'http://www.shu800.com/xinggan/index_63.html',
        'http://www.shu800.com/xinggan/index_64.html',
        'http://www.shu800.com/xinggan/index_65.html',
        'http://www.shu800.com/xinggan/index_66.html',
        'http://www.shu800.com/xinggan/index_67.html',
        'http://www.shu800.com/xinggan/index_68.html',
        'http://www.shu800.com/xinggan/index_69.html',

        'http://www.shu800.com/xinggan/index_70.html',
        'http://www.shu800.com/xinggan/index_71.html',
        'http://www.shu800.com/xinggan/index_72.html',
        'http://www.shu800.com/xinggan/index_73.html',
        'http://www.shu800.com/xinggan/index_74.html',
        'http://www.shu800.com/xinggan/index_75.html',
        'http://www.shu800.com/xinggan/index_76.html',
        'http://www.shu800.com/xinggan/index_77.html',
        'http://www.shu800.com/xinggan/index_78.html',
        'http://www.shu800.com/xinggan/index_79.html',

        'http://www.shu800.com/xinggan/index_80.html',
        'http://www.shu800.com/xinggan/index_81.html',
        'http://www.shu800.com/xinggan/index_82.html',
        'http://www.shu800.com/xinggan/index_83.html',
        'http://www.shu800.com/xinggan/index_84.html',
        'http://www.shu800.com/xinggan/index_85.html',
        'http://www.shu800.com/xinggan/index_86.html',
        'http://www.shu800.com/xinggan/index_87.html',
        'http://www.shu800.com/xinggan/index_88.html',
        'http://www.shu800.com/xinggan/index_89.html',

        'http://www.shu800.com/xinggan/index_90.html',
        'http://www.shu800.com/xinggan/index_91.html',
        'http://www.shu800.com/xinggan/index_92.html',
        'http://www.shu800.com/xinggan/index_93.html',
        'http://www.shu800.com/xinggan/index_94.html',
        'http://www.shu800.com/xinggan/index_95.html',
        'http://www.shu800.com/xinggan/index_96.html',
        'http://www.shu800.com/xinggan/index_97.html',
        'http://www.shu800.com/xinggan/index_98.html',
        'http://www.shu800.com/xinggan/index_99.html',

        'http://www.shu800.com/xinggan/index_100.html',
        'http://www.shu800.com/xinggan/index_101.html',
        'http://www.shu800.com/xinggan/index_102.html',
        'http://www.shu800.com/xinggan/index_103.html',
        'http://www.shu800.com/xinggan/index_104.html',
        'http://www.shu800.com/xinggan/index_105.html',
        'http://www.shu800.com/xinggan/index_106.html',
        'http://www.shu800.com/xinggan/index_107.html',
        'http://www.shu800.com/xinggan/index_108.html',
        'http://www.shu800.com/xinggan/index_109.html',

        'http://www.shu800.com/xinggan/index_110.html',
        'http://www.shu800.com/xinggan/index_111.html',
        'http://www.shu800.com/xinggan/index_112.html',
        'http://www.shu800.com/xinggan/index_113.html',
        'http://www.shu800.com/xinggan/index_114.html',
        'http://www.shu800.com/xinggan/index_115.html',
        'http://www.shu800.com/xinggan/index_116.html',
        'http://www.shu800.com/xinggan/index_117.html',
        'http://www.shu800.com/xinggan/index_118.html',
        'http://www.shu800.com/xinggan/index_119.html',

        'http://www.shu800.com/xinggan/index_120.html',
        'http://www.shu800.com/xinggan/index_121.html',
        'http://www.shu800.com/xinggan/index_122.html',
        'http://www.shu800.com/xinggan/index_123.html',
        'http://www.shu800.com/xinggan/index_124.html',
        'http://www.shu800.com/xinggan/index_125.html',
        'http://www.shu800.com/xinggan/index_126.html',
        'http://www.shu800.com/xinggan/index_127.html',
        'http://www.shu800.com/xinggan/index_128.html',
        'http://www.shu800.com/xinggan/index_129.html',

        'http://www.shu800.com/xinggan/index_130.html',
        'http://www.shu800.com/xinggan/index_131.html',
        'http://www.shu800.com/xinggan/index_132.html',
        'http://www.shu800.com/xinggan/index_133.html',
        'http://www.shu800.com/xinggan/index_134.html',
        'http://www.shu800.com/xinggan/index_135.html',
        'http://www.shu800.com/xinggan/index_136.html',
        'http://www.shu800.com/xinggan/index_137.html',
        'http://www.shu800.com/xinggan/index_138.html',
        'http://www.shu800.com/xinggan/index_139.html',

        'http://www.shu800.com/xinggan/index_140.html',
        'http://www.shu800.com/xinggan/index_141.html',
        'http://www.shu800.com/xinggan/index_142.html',
        'http://www.shu800.com/xinggan/index_143.html',
        'http://www.shu800.com/xinggan/index_144.html',
        'http://www.shu800.com/xinggan/index_145.html',
        'http://www.shu800.com/xinggan/index_146.html',
        'http://www.shu800.com/xinggan/index_147.html',
        'http://www.shu800.com/xinggan/index_148.html',
        'http://www.shu800.com/xinggan/index_149.html',

        'http://www.shu800.com/xinggan/index_150.html',
        'http://www.shu800.com/xinggan/index_151.html',
        'http://www.shu800.com/xinggan/index_152.html',
        'http://www.shu800.com/xinggan/index_153.html',
        'http://www.shu800.com/xinggan/index_154.html',
        'http://www.shu800.com/xinggan/index_155.html',
        'http://www.shu800.com/xinggan/index_156.html',
        'http://www.shu800.com/xinggan/index_157.html',
        'http://www.shu800.com/xinggan/index_158.html',
        'http://www.shu800.com/xinggan/index_159.html',

        'http://www.shu800.com/xinggan/index_160.html',
        'http://www.shu800.com/xinggan/index_161.html',
        'http://www.shu800.com/xinggan/index_162.html',
        'http://www.shu800.com/xinggan/index_163.html',
        'http://www.shu800.com/xinggan/index_164.html',
        'http://www.shu800.com/xinggan/index_165.html',
        'http://www.shu800.com/xinggan/index_166.html',
        'http://www.shu800.com/xinggan/index_167.html',
        'http://www.shu800.com/xinggan/index_168.html',
        'http://www.shu800.com/xinggan/index_169.html',

        'http://www.shu800.com/xinggan/index_170.html',
        'http://www.shu800.com/xinggan/index_171.html',
        'http://www.shu800.com/xinggan/index_172.html',
        'http://www.shu800.com/xinggan/index_173.html',
        'http://www.shu800.com/xinggan/index_174.html',
        'http://www.shu800.com/xinggan/index_175.html',
        'http://www.shu800.com/xinggan/index_176.html',
        'http://www.shu800.com/xinggan/index_177.html',
        'http://www.shu800.com/xinggan/index_178.html',
        'http://www.shu800.com/xinggan/index_179.html',

        'http://www.shu800.com/xinggan/index_180.html',
        'http://www.shu800.com/xinggan/index_181.html',
        'http://www.shu800.com/xinggan/index_182.html',
        'http://www.shu800.com/xinggan/index_183.html',
        'http://www.shu800.com/xinggan/index_184.html',
        'http://www.shu800.com/xinggan/index_185.html',
        'http://www.shu800.com/xinggan/index_186.html',
        'http://www.shu800.com/xinggan/index_187.html',
        'http://www.shu800.com/xinggan/index_188.html',
        'http://www.shu800.com/xinggan/index_189.html',

        'http://www.shu800.com/xinggan/index_190.html',
        'http://www.shu800.com/xinggan/index_191.html',
        'http://www.shu800.com/xinggan/index_192.html',
        'http://www.shu800.com/xinggan/index_193.html',
        'http://www.shu800.com/xinggan/index_194.html',
        'http://www.shu800.com/xinggan/index_195.html',
        'http://www.shu800.com/xinggan/index_196.html',
        'http://www.shu800.com/xinggan/index_197.html',
        'http://www.shu800.com/xinggan/index_198.html',
        'http://www.shu800.com/xinggan/index_199.html',

        'http://www.shu800.com/xinggan/index_200.html',
        'http://www.shu800.com/xinggan/index_201.html',
        'http://www.shu800.com/xinggan/index_202.html',
        'http://www.shu800.com/xinggan/index_203.html',
        'http://www.shu800.com/xinggan/index_204.html',
        'http://www.shu800.com/xinggan/index_205.html',
        'http://www.shu800.com/xinggan/index_206.html',
        'http://www.shu800.com/xinggan/index_207.html',
        'http://www.shu800.com/xinggan/index_208.html',
        'http://www.shu800.com/xinggan/index_209.html',

        'http://www.shu800.com/xinggan/index_210.html',
        'http://www.shu800.com/xinggan/index_211.html',
        'http://www.shu800.com/xinggan/index_212.html',
        'http://www.shu800.com/xinggan/index_213.html',
        'http://www.shu800.com/xinggan/index_214.html',
        'http://www.shu800.com/xinggan/index_215.html',
        'http://www.shu800.com/xinggan/index_216.html',
        'http://www.shu800.com/xinggan/index_217.html',
        'http://www.shu800.com/xinggan/index_218.html',
        'http://www.shu800.com/xinggan/index_219.html',

        'http://www.shu800.com/xinggan/index_220.html',
        'http://www.shu800.com/xinggan/index_221.html',
        'http://www.shu800.com/xinggan/index_222.html',
        'http://www.shu800.com/xinggan/index_223.html',
        'http://www.shu800.com/xinggan/index_224.html',
        'http://www.shu800.com/xinggan/index_225.html',
        'http://www.shu800.com/xinggan/index_226.html',
        'http://www.shu800.com/xinggan/index_227.html',
        'http://www.shu800.com/xinggan/index_228.html',
        'http://www.shu800.com/xinggan/index_229.html',

        'http://www.shu800.com/xinggan/index_230.html',
        'http://www.shu800.com/xinggan/index_231.html',
        'http://www.shu800.com/xinggan/index_232.html',
        'http://www.shu800.com/xinggan/index_233.html',
        'http://www.shu800.com/xinggan/index_234.html',
        'http://www.shu800.com/xinggan/index_235.html',
        'http://www.shu800.com/xinggan/index_236.html',
        'http://www.shu800.com/xinggan/index_237.html',
        'http://www.shu800.com/xinggan/index_238.html',
        'http://www.shu800.com/xinggan/index_239.html',

        'http://www.shu800.com/xinggan/index_240.html',
        'http://www.shu800.com/xinggan/index_241.html',
        'http://www.shu800.com/xinggan/index_242.html',
        'http://www.shu800.com/xinggan/index_243.html',
        'http://www.shu800.com/xinggan/index_244.html',
        'http://www.shu800.com/xinggan/index_245.html',
        'http://www.shu800.com/xinggan/index_246.html',
        'http://www.shu800.com/xinggan/index_247.html',
        'http://www.shu800.com/xinggan/index_248.html',
        'http://www.shu800.com/xinggan/index_249.html',

        'http://www.shu800.com/xinggan/index_250.html',
        'http://www.shu800.com/xinggan/index_251.html',
        'http://www.shu800.com/xinggan/index_252.html',
        'http://www.shu800.com/xinggan/index_253.html',
        'http://www.shu800.com/xinggan/index_254.html',
        'http://www.shu800.com/xinggan/index_255.html',
        'http://www.shu800.com/xinggan/index_256.html',
        'http://www.shu800.com/xinggan/index_257.html',
        'http://www.shu800.com/xinggan/index_258.html',
        'http://www.shu800.com/xinggan/index_259.html',

        'http://www.shu800.com/xinggan/index_260.html',
        'http://www.shu800.com/xinggan/index_261.html',
        'http://www.shu800.com/xinggan/index_262.html',
        'http://www.shu800.com/xinggan/index_263.html',
        'http://www.shu800.com/xinggan/index_264.html',
        'http://www.shu800.com/xinggan/index_265.html',
        'http://www.shu800.com/xinggan/index_266.html',
        'http://www.shu800.com/xinggan/index_267.html',
        'http://www.shu800.com/xinggan/index_268.html',
        'http://www.shu800.com/xinggan/index_269.html',

        'http://www.shu800.com/xinggan/index_270.html',
        'http://www.shu800.com/xinggan/index_271.html',
        'http://www.shu800.com/xinggan/index_272.html',
        'http://www.shu800.com/xinggan/index_273.html',
        'http://www.shu800.com/xinggan/index_274.html',
        'http://www.shu800.com/xinggan/index_275.html',
        'http://www.shu800.com/xinggan/index_276.html',
        'http://www.shu800.com/xinggan/index_277.html',
        'http://www.shu800.com/xinggan/index_278.html',
        'http://www.shu800.com/xinggan/index_279.html',

        'http://www.shu800.com/xinggan/index_280.html',
        'http://www.shu800.com/xinggan/index_281.html',
        'http://www.shu800.com/xinggan/index_282.html',
        'http://www.shu800.com/xinggan/index_283.html',
        'http://www.shu800.com/xinggan/index_284.html',
        'http://www.shu800.com/xinggan/index_285.html',
        'http://www.shu800.com/xinggan/index_286.html',
        'http://www.shu800.com/xinggan/index_287.html',
        'http://www.shu800.com/xinggan/index_288.html',
        'http://www.shu800.com/xinggan/index_289.html',

        'http://www.shu800.com/xinggan/index_290.html',
        'http://www.shu800.com/xinggan/index_291.html',
        'http://www.shu800.com/xinggan/index_292.html',
        'http://www.shu800.com/xinggan/index_293.html',
        'http://www.shu800.com/xinggan/index_294.html',
        'http://www.shu800.com/xinggan/index_295.html',
        'http://www.shu800.com/xinggan/index_296.html',
        'http://www.shu800.com/xinggan/index_297.html',
        'http://www.shu800.com/xinggan/index_298.html',
        'http://www.shu800.com/xinggan/index_299.html',

        'http://www.shu800.com/xinggan/index_300.html',
        'http://www.shu800.com/xinggan/index_301.html',
        'http://www.shu800.com/xinggan/index_302.html',
        'http://www.shu800.com/xinggan/index_303.html',
        'http://www.shu800.com/xinggan/index_304.html',
        'http://www.shu800.com/xinggan/index_305.html',
        'http://www.shu800.com/xinggan/index_306.html',
        'http://www.shu800.com/xinggan/index_307.html',
        'http://www.shu800.com/xinggan/index_308.html',
        'http://www.shu800.com/xinggan/index_309.html',

        'http://www.shu800.com/xinggan/index_310.html',
        'http://www.shu800.com/xinggan/index_311.html',
        'http://www.shu800.com/xinggan/index_312.html',
        'http://www.shu800.com/xinggan/index_313.html',
        'http://www.shu800.com/xinggan/index_314.html',
        'http://www.shu800.com/xinggan/index_315.html',
        'http://www.shu800.com/xinggan/index_316.html',
        'http://www.shu800.com/xinggan/index_317.html',
        'http://www.shu800.com/xinggan/index_318.html',
        'http://www.shu800.com/xinggan/index_319.html',

        'http://www.shu800.com/xinggan/index_320.html',
        'http://www.shu800.com/xinggan/index_321.html',
        'http://www.shu800.com/xinggan/index_322.html',
        'http://www.shu800.com/xinggan/index_323.html',
        'http://www.shu800.com/xinggan/index_324.html',
        'http://www.shu800.com/xinggan/index_325.html',
        'http://www.shu800.com/xinggan/index_326.html',
        'http://www.shu800.com/xinggan/index_327.html',
        'http://www.shu800.com/xinggan/index_328.html',
        'http://www.shu800.com/xinggan/index_329.html',

        'http://www.shu800.com/xinggan/index_330.html',
        'http://www.shu800.com/xinggan/index_331.html',
        'http://www.shu800.com/xinggan/index_332.html',
        'http://www.shu800.com/xinggan/index_333.html',
        'http://www.shu800.com/xinggan/index_334.html',
        'http://www.shu800.com/xinggan/index_335.html',
        'http://www.shu800.com/xinggan/index_336.html',
        'http://www.shu800.com/xinggan/index_337.html',
        'http://www.shu800.com/xinggan/index_338.html',
        'http://www.shu800.com/xinggan/index_339.html',

        'http://www.shu800.com/xinggan/index_340.html',
        'http://www.shu800.com/xinggan/index_341.html',
        'http://www.shu800.com/xinggan/index_342.html',
        'http://www.shu800.com/xinggan/index_343.html',
        'http://www.shu800.com/xinggan/index_344.html',
        'http://www.shu800.com/xinggan/index_345.html',
        'http://www.shu800.com/xinggan/index_346.html',
        'http://www.shu800.com/xinggan/index_347.html',
        'http://www.shu800.com/xinggan/index_348.html',
        'http://www.shu800.com/xinggan/index_349.html',

        'http://www.shu800.com/xinggan/index_350.html',
        'http://www.shu800.com/xinggan/index_351.html',
        'http://www.shu800.com/xinggan/index_352.html',
        'http://www.shu800.com/xinggan/index_353.html',
        'http://www.shu800.com/xinggan/index_354.html',
        'http://www.shu800.com/xinggan/index_355.html',
        'http://www.shu800.com/xinggan/index_356.html',
        'http://www.shu800.com/xinggan/index_357.html',
        'http://www.shu800.com/xinggan/index_358.html',
        'http://www.shu800.com/xinggan/index_359.html',

        'http://www.shu800.com/xinggan/index_360.html',
        'http://www.shu800.com/xinggan/index_361.html',
        'http://www.shu800.com/xinggan/index_362.html',
        'http://www.shu800.com/xinggan/index_363.html',
        'http://www.shu800.com/xinggan/index_364.html',
        'http://www.shu800.com/xinggan/index_365.html',
        'http://www.shu800.com/xinggan/index_366.html',
        'http://www.shu800.com/xinggan/index_367.html',
        'http://www.shu800.com/xinggan/index_368.html',
        'http://www.shu800.com/xinggan/index_369.html',

        'http://www.shu800.com/xinggan/index_370.html',
        'http://www.shu800.com/xinggan/index_371.html',
        'http://www.shu800.com/xinggan/index_372.html',
        'http://www.shu800.com/xinggan/index_373.html',
        'http://www.shu800.com/xinggan/index_374.html',
        'http://www.shu800.com/xinggan/index_375.html',
        'http://www.shu800.com/xinggan/index_376.html',
        'http://www.shu800.com/xinggan/index_377.html',
        'http://www.shu800.com/xinggan/index_378.html',
        'http://www.shu800.com/xinggan/index_379.html',

        'http://www.shu800.com/xinggan/index_380.html',
        'http://www.shu800.com/xinggan/index_381.html',
        'http://www.shu800.com/xinggan/index_382.html',
        'http://www.shu800.com/xinggan/index_383.html',
        'http://www.shu800.com/xinggan/index_384.html',
        'http://www.shu800.com/xinggan/index_385.html',
        'http://www.shu800.com/xinggan/index_386.html',
        'http://www.shu800.com/xinggan/index_387.html',
        'http://www.shu800.com/xinggan/index_388.html',
        'http://www.shu800.com/xinggan/index_389.html',

        'http://www.shu800.com/xinggan/index_390.html',
        'http://www.shu800.com/xinggan/index_391.html',
        'http://www.shu800.com/xinggan/index_392.html',
        'http://www.shu800.com/xinggan/index_393.html',
        'http://www.shu800.com/xinggan/index_394.html',
        'http://www.shu800.com/xinggan/index_395.html',
        'http://www.shu800.com/xinggan/index_396.html',
        'http://www.shu800.com/xinggan/index_397.html',
        'http://www.shu800.com/xinggan/index_398.html',
        'http://www.shu800.com/xinggan/index_399.html',

        'http://www.shu800.com/xinggan/index_400.html',
        'http://www.shu800.com/xinggan/index_401.html',
        'http://www.shu800.com/xinggan/index_402.html',
        'http://www.shu800.com/xinggan/index_403.html',
        'http://www.shu800.com/xinggan/index_404.html',
        'http://www.shu800.com/xinggan/index_405.html',
        'http://www.shu800.com/xinggan/index_406.html',
        'http://www.shu800.com/xinggan/index_407.html',
        'http://www.shu800.com/xinggan/index_408.html',
        'http://www.shu800.com/xinggan/index_409.html',

        'http://www.shu800.com/xinggan/index_410.html',
        'http://www.shu800.com/xinggan/index_411.html',
        'http://www.shu800.com/xinggan/index_412.html',
        'http://www.shu800.com/xinggan/index_413.html',
        'http://www.shu800.com/xinggan/index_414.html',
        'http://www.shu800.com/xinggan/index_415.html',
        'http://www.shu800.com/xinggan/index_416.html',
        'http://www.shu800.com/xinggan/index_417.html',
        'http://www.shu800.com/xinggan/index_418.html',
        'http://www.shu800.com/xinggan/index_419.html',

        'http://www.shu800.com/xinggan/index_420.html',
        'http://www.shu800.com/xinggan/index_421.html',
        'http://www.shu800.com/xinggan/index_422.html'
    ]

    #这个有水印，取消

    def parse(self, response):
        print(response.text)
        imglist = response.xpath("//ul[@class='detail-list']/li")
        for item in imglist:
            print(item)
            # 创建一个变量 item文件导进来
            img_itme = PythondemoItem()
            img_itme['imgsrc'] = item.xpath(".//img/@src").extract_first()
            #    把数据yield到管道中去
            yield img_itme
