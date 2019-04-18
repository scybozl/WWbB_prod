
TOPMASS=mt171p0

c=1;
for i in $(cat input.txt) ; do
  echo $i &&
  cp mppui_batch.sbx submit/mppui_batch-$TOPMASS-$c.sbx &&
  sed -i "s|FILE=bb4l-powhegpwgevents._00001.lhe.events.root|FILE=$i|g" submit/mppui_batch-$TOPMASS-$c.sbx &&
  sed -i "s|TOPMASS=mt171p0|TOPMASS=$TOPMASS|g" submit/mppui_batch-$TOPMASS-$c.sbx &&
  sbatch submit/mppui_batch-$TOPMASS-$c.sbx && c=$((c+1));
done

