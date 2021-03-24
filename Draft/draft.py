"""
        allTestCasesInFolderIncludeSubfolders = []

        def extractFolders(folders):
            for folder in folders:
                print(folder.Name)
                print("---")
                extractTestCasesFromFolder(folder)


        def extractTestCasesFromFolder(folder):
            if len(folder.TestCases) > 0:
                for testCase in folder.TestCases: 
                    print(testCase.Name)
                if len(folder.Children) > 0:
                    extractFolders(folder.Children)

        #login

        user = UserCredential(server, login, password)
        rally = RallyInstance(user).rally
        #set workspace
        workspaces = rally.getWorkspaces()
        rally.setWorkspace('')
        rally.setProject('')
        #set root folder
        rootFolder = RallyFolder(rally ,'FormattedID = ""').testFolder #
        #get all folders from root folder
        folders = rootFolder.Children
        #prepare list of bars
        bars = TestsAndFoldersActions().extractFoldersFromRootFolder(rootFolder)
        tidyData = DataFrameActions.PrepareDataFrame(bars)

        names = []
        manual = []
        automated = []
        for bar in bars:
            names.append(bar.headFolderdName)
            manual.append(bar.countManualTestCases)
            automated.append(bar.countAutomatedTestCases)

        df = pd.DataFrame({
            'Factor': names,
            'Weight': manual,
            'Weight2': automated
        })

        countTestCases = manual + automated
        maxAxisX = max(countTestCases) + 1

        plt.rcParams.update({'figure.autolayout': True})
        tidy = df.melt(id_vars='Factor').rename(columns=str.title)

        plt.rcParams.update({'figure.autolayout': True})
        ax = sns.barplot(y='Factor', x='Value', hue='Variable', data=tidyData)
        maxAxisX = TestsAndFoldersActions.getMaxValueTestCases(bars)
        ax.set_xlim(0, maxAxisX)
        ax.set_xticks(range(0, maxAxisX))
        mplcursors.cursor(ax, hover=False).connect("add", lambda sel: sel.annotation.set_text(print("bar is: " + str(sel.target.index + 1))))
        plt.show()

        list_steps = None
        for test_case in test_cases:
            print(test_case.FormattedID)
            print(test_case.Name)
            list_steps=test_case.Steps
            listInputs = []
            listExpectedResult = []
            for i in list_steps:
                listInputs.append(i.Input)
                print(i.Input)
            for er in list_steps:
                listExpectedResult.append(er.ExpectedResult)
                print(er.ExpectedResult)

        #It looks like this cut off some of the labels on the bottom. We can tell Matplotlib to automatically make room for elements in the figures that we create
        plt.rcParams.update({'figure.autolayout': True})

        pylab.rcParams['ytick.major.pad']='8'

        fig, ax = plt.subplots()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        lx = []
        ly = []
        labels = []

        for b in bars:
            lx.append(b.x)
            ly.append(b.countManualTestCases)
            labels.append(b.headFolderdName)

        #ax.set(yticks = range(1, len(lx) + 1), yticklabels = labels, title="Hover over a bar")
        ax.set(yticks = range(1, len(ly) + 1), yticklabels = labels, title="Hover over a bar")
        #ax.barh(lx, ly, align="center")
        ax.barh(lx, ly, height=0.01, align="center")
    """
