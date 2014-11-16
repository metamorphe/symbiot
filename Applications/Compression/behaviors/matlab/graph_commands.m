% data = readcsv('behaviors.csv', ',');
% n = size(data, 1);
% names = {}
% for i=1:n
%     if mod(i, 3) == 1
%         j = ceil(i/3);
%         names{j} = data{i};
%         data{i} = {};
%     end
% end

files = dir('*.csv');
names = {};
i = 1;

for file = files'
    name = strsplit(file.name, '_')
    behaviors{i, 1} = name{1};
    file.name
    behaviors{i, 2} = csvread(file.name);
    i = i + 1;
end

n = size(behaviors, 1)
figure
i = 1
for b = behaviors'
    subplot(8, 3, i);
    commands = b{2};
    scatter(commands(2, :), commands(1, :),5, 'filled');
    i = i + 1;
    title(b{1})
    xlabel('t')
    ylabel('I')
    axis([0, max(commands(2, :)) + 20, 0, 300]) 
    set(gca, 'YTick', [0:255:255])
end





