# Forest: Other5's own ground and sky materials in place of the Megascans gravel surface and sky dome.
# M_ForestGround: Cozy Nature's grass textures, world-aligned (no UV needs). M_ForestSky: an unlit gradient. Rerunnable.
import unreal
Lib = unreal.MaterialEditingLibrary
Tools = unreal.AssetToolsHelpers.get_asset_tools()
Folder = "/Other5ForestBiome_Minimal/Materials"
def Fresh(Name):
	P = "%s/%s" % (Folder, Name)
	if unreal.EditorAssetLibrary.does_asset_exist(P):
		M = unreal.EditorAssetLibrary.load_asset(P); Lib.delete_all_material_expressions(M); return M
	return Tools.create_asset(Name, Folder, unreal.Material, unreal.MaterialFactoryNew())
def Fn(M, Path, X, Y):
	F = Lib.create_material_expression(M, unreal.MaterialExpressionMaterialFunctionCall, X, Y)
	F.set_editor_property("material_function", unreal.load_asset(Path)); return F
def Tex(M, Path, X, Y):
	T = Lib.create_material_expression(M, unreal.MaterialExpressionTextureObject, X, Y)
	T.set_editor_property("texture", unreal.load_asset(Path)); return T
def Const(M, V, X, Y):
	C = Lib.create_material_expression(M, unreal.MaterialExpressionConstant, X, Y); C.set_editor_property("r", V); return C
WAT = "/Engine/Functions/Engine_MaterialFunctions01/Texturing/WorldAlignedTexture.WorldAlignedTexture"
G = Fresh("M_ForestGround")
Size = Const(G, 400.0, -900, 300)
for Tx, Prop, Y in (("/Other5ForestBiome_Minimal/CozyNature/Textures/Terrain/T_Grass_BC.T_Grass_BC", unreal.MaterialProperty.MP_BASE_COLOR, 0),
		("/Other5ForestBiome_Minimal/CozyNature/Textures/Terrain/T_Grass_N.T_Grass_N", unreal.MaterialProperty.MP_NORMAL, 400)):
	W = Fn(G, WAT, -400, Y)
	Lib.connect_material_expressions(Tex(G, Tx, -800, Y), "", W, "TextureObject")
	Lib.connect_material_expressions(Size, "", W, "TextureSize")
	Lib.connect_material_property(W, "XYZ Texture", Prop)
Lib.connect_material_property(Const(G, 0.9, -300, 800), "", unreal.MaterialProperty.MP_ROUGHNESS)
Lib.recompile_material(G); unreal.EditorAssetLibrary.save_loaded_asset(G)
S = Fresh("M_ForestSky")
S.set_editor_property("shading_model", unreal.MaterialShadingModel.MSM_UNLIT)
S.set_editor_property("two_sided", True)
N = Lib.create_material_expression(S, unreal.MaterialExpressionVertexNormalWS, -900, 0)
Mask = Lib.create_material_expression(S, unreal.MaterialExpressionComponentMask, -750, 0)
Mask.set_editor_property("r", False); Mask.set_editor_property("g", False); Mask.set_editor_property("b", True)
Lib.connect_material_expressions(N, "", Mask, "")
Abs = Lib.create_material_expression(S, unreal.MaterialExpressionAbs, -600, 0); Lib.connect_material_expressions(Mask, "", Abs, "")
Lerp = Lib.create_material_expression(S, unreal.MaterialExpressionLinearInterpolate, -300, 0)
A = Lib.create_material_expression(S, unreal.MaterialExpressionConstant3Vector, -600, -200); A.set_editor_property("constant", unreal.LinearColor(0.75, 0.85, 0.95, 1))
B = Lib.create_material_expression(S, unreal.MaterialExpressionConstant3Vector, -600, 200); B.set_editor_property("constant", unreal.LinearColor(0.25, 0.45, 0.85, 1))
Lib.connect_material_expressions(A, "", Lerp, "A"); Lib.connect_material_expressions(B, "", Lerp, "B"); Lib.connect_material_expressions(Abs, "", Lerp, "Alpha")
Lib.connect_material_property(Lerp, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)
Lib.recompile_material(S); unreal.EditorAssetLibrary.save_loaded_asset(S)
unreal.log("OwnGround: made M_ForestGround and M_ForestSky")
