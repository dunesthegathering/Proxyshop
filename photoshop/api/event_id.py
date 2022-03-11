# Import built-in modules
from enum import Enum


class EventID(str, Enum):
    # Here is a list of JSON CallBack events in Photoshop.
    # https://community.adobe.com/t5/get-started/photoshop-json-callback-events-list-up-to-cc2015-ver-16/td-p/4792115?page=1
    TDTransform = "TdT "
    Average = "Avrg"
    ApplyStyle = "ASty"
    Assert = "Asrt"
    AccentedEdges = "AccE"
    Add = "Add"
    AddNoise = "AdNs"
    AddTo = "AddT"
    Align = "Algn"
    All = "All "
    AngledStrokes = "AngS"
    ApplyImage = "AppI"
    BasRelief = "BsRl"
    Batch = "Btch"
    BatchFromDroplet = "BtcF"
    Blur = "Blr "
    BlurMore = "BlrM"
    Border = "Brdr"
    Brightness = "BrgC"
    CanvasSize = "CnvS"
    ChalkCharcoal = "ChlC"
    ChannelMixer = "ChnM"
    Charcoal = "Chrc"
    Chrome = "Chrm"
    Clear = "Cler"
    Close = "Cls "
    Clouds = "Clds"
    ColorBalance = "ClrB"
    ColorHalftone = "ClrH"
    ColorRange = "ClrR"
    ColoredPencil = "ClrP"
    ContactSheet = "0B71D221-F8CE-11d2-B21B-0008C75B322C"
    ConteCrayon = "CntC"
    Contract = "Cntc"
    ConvertMode = "CnvM"
    Copy = "copy"
    CopyEffects = "CpFX"
    CopyMerged = "CpyM"
    CopyToLayer = "CpTL"
    Craquelure = "Crql"
    CreateDroplet = "CrtD"
    Crop = "Crop"
    Crosshatch = "Crsh"
    Crystallize = "Crst"
    Curves = "Crvs"
    Custom = "Cstm"
    Cut = "cut "
    CutToLayer = "CtTL"
    Cutout = "Ct  "
    DarkStrokes = "DrkS"
    DeInterlace = "Dntr"
    DefinePattern = "DfnP"
    Defringe = "Dfrg"
    Delete = "Dlt "
    Desaturate = "Dstt"
    Deselect = "Dslc"
    Despeckle = "Dspc"
    DifferenceClouds = "DrfC"
    Diffuse = "Dfs "
    DiffuseGlow = "DfsG"
    DisableLayerFX = "dlfx"
    Displace = "Dspl"
    Distribute = "Dstr"
    Draw = "Draw"
    DryBrush = "DryB"
    Duplicate = "Dplc"
    DustAndScratches = "DstS"
    Emboss = "Embs"
    Equalize = "Eqlz"
    Exchange = "Exch"
    Expand = "Expn"
    Export = "Expr"
    Jumpto = "Jpto"
    ExportTransparentImage = "02879e00-cb66-11d1-bc43-0060b0a13dc4"
    Extrude = "Extr"
    Facet = "Fct "
    Fade = "Fade"
    Feather = "Fthr"
    Fibers = "Fbrs"
    Fill = "Fl  "
    FilmGrain = "FlmG"
    Filter = "Fltr"
    FindEdges = "FndE"
    FitImage = "3caa3434-cb67-11d1-bc43-0060b0a13dc4"
    FlattenImage = "FltI"
    Flip = "Flip"
    Fragment = "Frgm"
    Fresco = "Frsc"
    GaussianBlur = "GsnB"
    Get = "getd"
    Glass = "Gls "
    GlowingEdges = "GlwE"
    Gradient = "Grdn"
    GradientMap = "GrMp"
    Grain = "Grn "
    GraphicPen = "GraP"
    Group = "GrpL"
    Grow = "Grow"
    HalftoneScreen = "HlfS"
    Hide = "Hd  "
    HighPass = "HghP"
    HSBHSL = "HsbP"
    HueSaturation = "HStr"
    ImageSize = "ImgS"
    Import = "Impr"
    InkOutlines = "InkO"
    Intersect = "Intr"
    IntersectWith = "IntW"
    Inverse = "Invs"
    Invert = "Invr"
    LensFlare = "LnsF"
    Levels = "Lvls"
    LightingEffects = "LghE"
    Link = "Lnk "
    Make = "Mk  "
    Maximum = "Mxm "
    Median = "Mdn "
    MergeLayers = "Mrg2"
    MergeLayersOld = "MrgL"
    MergeSpotChannel = "MSpt"
    MergeVisible = "MrgV"
    Mezzotint = "Mztn"
    Minimum = "Mnm "
    ModeChange = "8cba8cd6-cb66-11d1-bc43-0060b0a13dc4"
    Mosaic = "Msc "
    Mosaic_PLUGIN = "MscT"
    MotionBlur = "MtnB"
    Move = "move"
    NTSCColors = "NTSC"
    NeonGlow = "NGlw"
    Next = "Nxt "
    NotePaper = "NtPr"
    Notify = "Ntfy"
    Null = "typeNull"
    OceanRipple = "OcnR"
    Offset = "Ofst"
    Open = "Opn "
    Paint = "Pnt "
    PaintDaubs = "PntD"
    PaletteKnife = "PltK"
    Paste = "past"
    PasteEffects = "PaFX"
    PasteInto = "PstI"
    PasteOutside = "PstO"
    Patchwork = "Ptch"
    Photocopy = "Phtc"
    PicturePackage = "4C1ABF40-DD82-11d2-B20F-0008C75B322C"
    Pinch = "Pnch"
    Place = "Plc "
    Plaster = "Plst"
    PlasticWrap = "PlsW"
    Play = "Ply "
    Pointillize = "Pntl"
    Polar = "Plr "
    PosterEdges = "PstE"
    Posterize = "Pstr"
    Previous = "Prvs"
    Print = "Prnt"
    ProfileToProfile = "PrfT"
    Purge = "Prge"
    Quit = "quit"
    RadialBlur = "RdlB"
    Rasterize = "Rstr"
    RasterizeTypeSheet = "RstT"
    RemoveBlackMatte = "RmvB"
    RemoveLayerMask = "RmvL"
    RemoveWhiteMatte = "RmvW"
    Rename = "Rnm "
    ReplaceColor = "RplC"
    Reset = "Rset"
    ResizeImage = "1333cf0c-cb67-11d1-bc43-0060b0a13dc4"
    Reticulation = "Rtcl"
    Revert = "Rvrt"
    Ripple = "Rple"
    Rotate = "Rtte"
    RoughPastels = "RghP"
    Save = "save"
    Select = "slct"
    SelectiveColor = "SlcC"
    Set = "setd"
    SharpenEdges = "ShrE"
    Sharpen = "Shrp"
    SharpenMore = "ShrM"
    Shear = "Shr "
    Show = "Shw "
    Similar = "Smlr"
    SmartBlur = "SmrB"
    Smooth = "Smth"
    SmudgeStick = "SmdS"
    Solarize = "Slrz"
    Spatter = "Spt "
    Spherize = "Sphr"
    SplitChannels = "SplC"
    Sponge = "Spng"
    SprayedStrokes = "SprS"
    StainedGlass = "StnG"
    Stamp = "Stmp"
    Stop = "Stop"
    Stroke = "Strk"
    Subtract = "Sbtr"
    SubtractFrom = "SbtF"
    Sumie = "Smie"
    TakeMergedSnapshot = "TkMr"
    TakeSnapshot = "TkSn"
    TextureFill = "TxtF"
    Texturizer = "Txtz"
    Threshold = "Thrs"
    Tiles = "Tls "
    TornEdges = "TrnE"
    TraceContour = "TrcC"
    Transform = "Trnf"
    Trap = "Trap"
    Twirl = "Twrl"
    Underpainting = "Undr"
    Undo = "undo"
    Ungroup = "Ungr"
    Unlink = "Unlk"
    UnsharpMask = "UnsM"
    Variations = "Vrtn"
    Wait = "Wait"
    WaterPaper = "WtrP"
    Watercolor = "Wtrc"
    Wave = "Wave"
    Wind = "Wnd "
    ZigZag = "ZgZg"
    BackLight = "BacL"
    FillFlash = "FilE"
    ColorCast = "ColE"
    OpenUntitled = "OpnU"
    PresetKind = "presetKindType"
    SmartSharpen = "smartSharpen"
    PresetKindType = "presetKindType"
    PresetKindCustom = "presetKindCustom"
    NoiseReduction = "noiseReduction"
    BlurType = "blurType"
    ContentLayer = "contentLayer"
    SaveStage = "saveStage"
    SaveStageType = "saveStageType"
    SaveSucceeded = "saveSucceeded"
    RasterizeLayer = "rasterizeLayer"
    ForceNotify = "forceNotify"
    PlacedLayerEditContents = "placedLayerEditContents"
