% ply path
outputPath = '/Users/shanfandi/Desktop/CV_project/meshply/';
dataPath = '/Users/shanfandi/Desktop/CV_project/data/car/';
% all mat files
files = dir('/Users/shanfandi/Desktop/CV_project/data/car/*.mat');
lengthFile = length(files)

for i = 1:length(files)
    % car_xxx_mesh.mat
    matName = files(i).name;
    
    % car_xxx_mesh
    plyname = strcat(outputPath, matName(1:end-4), '.ply')
    
    % load mat file
    fileName = strcat(dataPath, matName);
    %load mesh
    matFile = load(fileName);
    mesh = matFile.mesh;
   
    % convert .mat file to .ply file
    % only foucus on faces and vertices
    plywrite(plyname, mesh.faces, mesh.vertices)
end
