@echo off
setlocal enabledelayedexpansion

set "names=musemachine_aiswaryavk artofai_amalusanthosh genialgears_bincypaul aibrainstorm_chanchalmk neuralimagination_christeenastanly aithinker_fathimasherin aiworkshop_geethumahasenan codeplayground_lintusebastian aismartlab_mounikapottapingera ideabuilder_nehnubasheer dreamfactory_nirmalam aivisionary_poojithaj automagician_pruthvirajmalyala synthetica_sambireddybommareddy creativespace_sandhyabathina aicoalesce_shalumolm deepthink_shivaleelapeddamanishi aiexplorer_srilathabasani"

for %%a in (!names!) do (
  mkdir "%%a"
  echo Created folder: %%a
)

echo All folders created successfully.
pause
