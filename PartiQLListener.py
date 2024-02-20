# Generated from PartiQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PartiQLParser import PartiQLParser
else:
    from PartiQLParser import PartiQLParser

# This class defines a complete listener for a parse tree produced by PartiQLParser.
class PartiQLListener(ParseTreeListener):

    # Enter a parse tree produced by PartiQLParser#root.
    def enterRoot(self, ctx:PartiQLParser.RootContext):
        pass

    # Exit a parse tree produced by PartiQLParser#root.
    def exitRoot(self, ctx:PartiQLParser.RootContext):
        pass


    # Enter a parse tree produced by PartiQLParser#QueryDql.
    def enterQueryDql(self, ctx:PartiQLParser.QueryDqlContext):
        pass

    # Exit a parse tree produced by PartiQLParser#QueryDql.
    def exitQueryDql(self, ctx:PartiQLParser.QueryDqlContext):
        pass


    # Enter a parse tree produced by PartiQLParser#QueryDml.
    def enterQueryDml(self, ctx:PartiQLParser.QueryDmlContext):
        pass

    # Exit a parse tree produced by PartiQLParser#QueryDml.
    def exitQueryDml(self, ctx:PartiQLParser.QueryDmlContext):
        pass


    # Enter a parse tree produced by PartiQLParser#QueryDdl.
    def enterQueryDdl(self, ctx:PartiQLParser.QueryDdlContext):
        pass

    # Exit a parse tree produced by PartiQLParser#QueryDdl.
    def exitQueryDdl(self, ctx:PartiQLParser.QueryDdlContext):
        pass


    # Enter a parse tree produced by PartiQLParser#QueryExec.
    def enterQueryExec(self, ctx:PartiQLParser.QueryExecContext):
        pass

    # Exit a parse tree produced by PartiQLParser#QueryExec.
    def exitQueryExec(self, ctx:PartiQLParser.QueryExecContext):
        pass


    # Enter a parse tree produced by PartiQLParser#explainOption.
    def enterExplainOption(self, ctx:PartiQLParser.ExplainOptionContext):
        pass

    # Exit a parse tree produced by PartiQLParser#explainOption.
    def exitExplainOption(self, ctx:PartiQLParser.ExplainOptionContext):
        pass


    # Enter a parse tree produced by PartiQLParser#asIdent.
    def enterAsIdent(self, ctx:PartiQLParser.AsIdentContext):
        pass

    # Exit a parse tree produced by PartiQLParser#asIdent.
    def exitAsIdent(self, ctx:PartiQLParser.AsIdentContext):
        pass


    # Enter a parse tree produced by PartiQLParser#atIdent.
    def enterAtIdent(self, ctx:PartiQLParser.AtIdentContext):
        pass

    # Exit a parse tree produced by PartiQLParser#atIdent.
    def exitAtIdent(self, ctx:PartiQLParser.AtIdentContext):
        pass


    # Enter a parse tree produced by PartiQLParser#byIdent.
    def enterByIdent(self, ctx:PartiQLParser.ByIdentContext):
        pass

    # Exit a parse tree produced by PartiQLParser#byIdent.
    def exitByIdent(self, ctx:PartiQLParser.ByIdentContext):
        pass


    # Enter a parse tree produced by PartiQLParser#symbolPrimitive.
    def enterSymbolPrimitive(self, ctx:PartiQLParser.SymbolPrimitiveContext):
        pass

    # Exit a parse tree produced by PartiQLParser#symbolPrimitive.
    def exitSymbolPrimitive(self, ctx:PartiQLParser.SymbolPrimitiveContext):
        pass


    # Enter a parse tree produced by PartiQLParser#dql.
    def enterDql(self, ctx:PartiQLParser.DqlContext):
        pass

    # Exit a parse tree produced by PartiQLParser#dql.
    def exitDql(self, ctx:PartiQLParser.DqlContext):
        pass


    # Enter a parse tree produced by PartiQLParser#execCommand.
    def enterExecCommand(self, ctx:PartiQLParser.ExecCommandContext):
        pass

    # Exit a parse tree produced by PartiQLParser#execCommand.
    def exitExecCommand(self, ctx:PartiQLParser.ExecCommandContext):
        pass


    # Enter a parse tree produced by PartiQLParser#ddl.
    def enterDdl(self, ctx:PartiQLParser.DdlContext):
        pass

    # Exit a parse tree produced by PartiQLParser#ddl.
    def exitDdl(self, ctx:PartiQLParser.DdlContext):
        pass


    # Enter a parse tree produced by PartiQLParser#CreateTable.
    def enterCreateTable(self, ctx:PartiQLParser.CreateTableContext):
        pass

    # Exit a parse tree produced by PartiQLParser#CreateTable.
    def exitCreateTable(self, ctx:PartiQLParser.CreateTableContext):
        pass


    # Enter a parse tree produced by PartiQLParser#CreateIndex.
    def enterCreateIndex(self, ctx:PartiQLParser.CreateIndexContext):
        pass

    # Exit a parse tree produced by PartiQLParser#CreateIndex.
    def exitCreateIndex(self, ctx:PartiQLParser.CreateIndexContext):
        pass


    # Enter a parse tree produced by PartiQLParser#DropTable.
    def enterDropTable(self, ctx:PartiQLParser.DropTableContext):
        pass

    # Exit a parse tree produced by PartiQLParser#DropTable.
    def exitDropTable(self, ctx:PartiQLParser.DropTableContext):
        pass


    # Enter a parse tree produced by PartiQLParser#DropIndex.
    def enterDropIndex(self, ctx:PartiQLParser.DropIndexContext):
        pass

    # Exit a parse tree produced by PartiQLParser#DropIndex.
    def exitDropIndex(self, ctx:PartiQLParser.DropIndexContext):
        pass


    # Enter a parse tree produced by PartiQLParser#DmlBaseWrapper.
    def enterDmlBaseWrapper(self, ctx:PartiQLParser.DmlBaseWrapperContext):
        pass

    # Exit a parse tree produced by PartiQLParser#DmlBaseWrapper.
    def exitDmlBaseWrapper(self, ctx:PartiQLParser.DmlBaseWrapperContext):
        pass


    # Enter a parse tree produced by PartiQLParser#DmlDelete.
    def enterDmlDelete(self, ctx:PartiQLParser.DmlDeleteContext):
        pass

    # Exit a parse tree produced by PartiQLParser#DmlDelete.
    def exitDmlDelete(self, ctx:PartiQLParser.DmlDeleteContext):
        pass


    # Enter a parse tree produced by PartiQLParser#DmlInsertReturning.
    def enterDmlInsertReturning(self, ctx:PartiQLParser.DmlInsertReturningContext):
        pass

    # Exit a parse tree produced by PartiQLParser#DmlInsertReturning.
    def exitDmlInsertReturning(self, ctx:PartiQLParser.DmlInsertReturningContext):
        pass


    # Enter a parse tree produced by PartiQLParser#DmlBase.
    def enterDmlBase(self, ctx:PartiQLParser.DmlBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#DmlBase.
    def exitDmlBase(self, ctx:PartiQLParser.DmlBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#dmlBaseCommand.
    def enterDmlBaseCommand(self, ctx:PartiQLParser.DmlBaseCommandContext):
        pass

    # Exit a parse tree produced by PartiQLParser#dmlBaseCommand.
    def exitDmlBaseCommand(self, ctx:PartiQLParser.DmlBaseCommandContext):
        pass


    # Enter a parse tree produced by PartiQLParser#pathSimple.
    def enterPathSimple(self, ctx:PartiQLParser.PathSimpleContext):
        pass

    # Exit a parse tree produced by PartiQLParser#pathSimple.
    def exitPathSimple(self, ctx:PartiQLParser.PathSimpleContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PathSimpleLiteral.
    def enterPathSimpleLiteral(self, ctx:PartiQLParser.PathSimpleLiteralContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PathSimpleLiteral.
    def exitPathSimpleLiteral(self, ctx:PartiQLParser.PathSimpleLiteralContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PathSimpleSymbol.
    def enterPathSimpleSymbol(self, ctx:PartiQLParser.PathSimpleSymbolContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PathSimpleSymbol.
    def exitPathSimpleSymbol(self, ctx:PartiQLParser.PathSimpleSymbolContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PathSimpleDotSymbol.
    def enterPathSimpleDotSymbol(self, ctx:PartiQLParser.PathSimpleDotSymbolContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PathSimpleDotSymbol.
    def exitPathSimpleDotSymbol(self, ctx:PartiQLParser.PathSimpleDotSymbolContext):
        pass


    # Enter a parse tree produced by PartiQLParser#replaceCommand.
    def enterReplaceCommand(self, ctx:PartiQLParser.ReplaceCommandContext):
        pass

    # Exit a parse tree produced by PartiQLParser#replaceCommand.
    def exitReplaceCommand(self, ctx:PartiQLParser.ReplaceCommandContext):
        pass


    # Enter a parse tree produced by PartiQLParser#upsertCommand.
    def enterUpsertCommand(self, ctx:PartiQLParser.UpsertCommandContext):
        pass

    # Exit a parse tree produced by PartiQLParser#upsertCommand.
    def exitUpsertCommand(self, ctx:PartiQLParser.UpsertCommandContext):
        pass


    # Enter a parse tree produced by PartiQLParser#removeCommand.
    def enterRemoveCommand(self, ctx:PartiQLParser.RemoveCommandContext):
        pass

    # Exit a parse tree produced by PartiQLParser#removeCommand.
    def exitRemoveCommand(self, ctx:PartiQLParser.RemoveCommandContext):
        pass


    # Enter a parse tree produced by PartiQLParser#insertCommandReturning.
    def enterInsertCommandReturning(self, ctx:PartiQLParser.InsertCommandReturningContext):
        pass

    # Exit a parse tree produced by PartiQLParser#insertCommandReturning.
    def exitInsertCommandReturning(self, ctx:PartiQLParser.InsertCommandReturningContext):
        pass


    # Enter a parse tree produced by PartiQLParser#InsertLegacy.
    def enterInsertLegacy(self, ctx:PartiQLParser.InsertLegacyContext):
        pass

    # Exit a parse tree produced by PartiQLParser#InsertLegacy.
    def exitInsertLegacy(self, ctx:PartiQLParser.InsertLegacyContext):
        pass


    # Enter a parse tree produced by PartiQLParser#Insert.
    def enterInsert(self, ctx:PartiQLParser.InsertContext):
        pass

    # Exit a parse tree produced by PartiQLParser#Insert.
    def exitInsert(self, ctx:PartiQLParser.InsertContext):
        pass


    # Enter a parse tree produced by PartiQLParser#OnConflictLegacy.
    def enterOnConflictLegacy(self, ctx:PartiQLParser.OnConflictLegacyContext):
        pass

    # Exit a parse tree produced by PartiQLParser#OnConflictLegacy.
    def exitOnConflictLegacy(self, ctx:PartiQLParser.OnConflictLegacyContext):
        pass


    # Enter a parse tree produced by PartiQLParser#OnConflict.
    def enterOnConflict(self, ctx:PartiQLParser.OnConflictContext):
        pass

    # Exit a parse tree produced by PartiQLParser#OnConflict.
    def exitOnConflict(self, ctx:PartiQLParser.OnConflictContext):
        pass


    # Enter a parse tree produced by PartiQLParser#conflictTarget.
    def enterConflictTarget(self, ctx:PartiQLParser.ConflictTargetContext):
        pass

    # Exit a parse tree produced by PartiQLParser#conflictTarget.
    def exitConflictTarget(self, ctx:PartiQLParser.ConflictTargetContext):
        pass


    # Enter a parse tree produced by PartiQLParser#constraintName.
    def enterConstraintName(self, ctx:PartiQLParser.ConstraintNameContext):
        pass

    # Exit a parse tree produced by PartiQLParser#constraintName.
    def exitConstraintName(self, ctx:PartiQLParser.ConstraintNameContext):
        pass


    # Enter a parse tree produced by PartiQLParser#conflictAction.
    def enterConflictAction(self, ctx:PartiQLParser.ConflictActionContext):
        pass

    # Exit a parse tree produced by PartiQLParser#conflictAction.
    def exitConflictAction(self, ctx:PartiQLParser.ConflictActionContext):
        pass


    # Enter a parse tree produced by PartiQLParser#doReplace.
    def enterDoReplace(self, ctx:PartiQLParser.DoReplaceContext):
        pass

    # Exit a parse tree produced by PartiQLParser#doReplace.
    def exitDoReplace(self, ctx:PartiQLParser.DoReplaceContext):
        pass


    # Enter a parse tree produced by PartiQLParser#doUpdate.
    def enterDoUpdate(self, ctx:PartiQLParser.DoUpdateContext):
        pass

    # Exit a parse tree produced by PartiQLParser#doUpdate.
    def exitDoUpdate(self, ctx:PartiQLParser.DoUpdateContext):
        pass


    # Enter a parse tree produced by PartiQLParser#updateClause.
    def enterUpdateClause(self, ctx:PartiQLParser.UpdateClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#updateClause.
    def exitUpdateClause(self, ctx:PartiQLParser.UpdateClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#setCommand.
    def enterSetCommand(self, ctx:PartiQLParser.SetCommandContext):
        pass

    # Exit a parse tree produced by PartiQLParser#setCommand.
    def exitSetCommand(self, ctx:PartiQLParser.SetCommandContext):
        pass


    # Enter a parse tree produced by PartiQLParser#setAssignment.
    def enterSetAssignment(self, ctx:PartiQLParser.SetAssignmentContext):
        pass

    # Exit a parse tree produced by PartiQLParser#setAssignment.
    def exitSetAssignment(self, ctx:PartiQLParser.SetAssignmentContext):
        pass


    # Enter a parse tree produced by PartiQLParser#deleteCommand.
    def enterDeleteCommand(self, ctx:PartiQLParser.DeleteCommandContext):
        pass

    # Exit a parse tree produced by PartiQLParser#deleteCommand.
    def exitDeleteCommand(self, ctx:PartiQLParser.DeleteCommandContext):
        pass


    # Enter a parse tree produced by PartiQLParser#returningClause.
    def enterReturningClause(self, ctx:PartiQLParser.ReturningClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#returningClause.
    def exitReturningClause(self, ctx:PartiQLParser.ReturningClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#returningColumn.
    def enterReturningColumn(self, ctx:PartiQLParser.ReturningColumnContext):
        pass

    # Exit a parse tree produced by PartiQLParser#returningColumn.
    def exitReturningColumn(self, ctx:PartiQLParser.ReturningColumnContext):
        pass


    # Enter a parse tree produced by PartiQLParser#FromClauseSimpleExplicit.
    def enterFromClauseSimpleExplicit(self, ctx:PartiQLParser.FromClauseSimpleExplicitContext):
        pass

    # Exit a parse tree produced by PartiQLParser#FromClauseSimpleExplicit.
    def exitFromClauseSimpleExplicit(self, ctx:PartiQLParser.FromClauseSimpleExplicitContext):
        pass


    # Enter a parse tree produced by PartiQLParser#FromClauseSimpleImplicit.
    def enterFromClauseSimpleImplicit(self, ctx:PartiQLParser.FromClauseSimpleImplicitContext):
        pass

    # Exit a parse tree produced by PartiQLParser#FromClauseSimpleImplicit.
    def exitFromClauseSimpleImplicit(self, ctx:PartiQLParser.FromClauseSimpleImplicitContext):
        pass


    # Enter a parse tree produced by PartiQLParser#whereClause.
    def enterWhereClause(self, ctx:PartiQLParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#whereClause.
    def exitWhereClause(self, ctx:PartiQLParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SelectAll.
    def enterSelectAll(self, ctx:PartiQLParser.SelectAllContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SelectAll.
    def exitSelectAll(self, ctx:PartiQLParser.SelectAllContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SelectItems.
    def enterSelectItems(self, ctx:PartiQLParser.SelectItemsContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SelectItems.
    def exitSelectItems(self, ctx:PartiQLParser.SelectItemsContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SelectValue.
    def enterSelectValue(self, ctx:PartiQLParser.SelectValueContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SelectValue.
    def exitSelectValue(self, ctx:PartiQLParser.SelectValueContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SelectPivot.
    def enterSelectPivot(self, ctx:PartiQLParser.SelectPivotContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SelectPivot.
    def exitSelectPivot(self, ctx:PartiQLParser.SelectPivotContext):
        pass


    # Enter a parse tree produced by PartiQLParser#projectionItems.
    def enterProjectionItems(self, ctx:PartiQLParser.ProjectionItemsContext):
        pass

    # Exit a parse tree produced by PartiQLParser#projectionItems.
    def exitProjectionItems(self, ctx:PartiQLParser.ProjectionItemsContext):
        pass


    # Enter a parse tree produced by PartiQLParser#projectionItem.
    def enterProjectionItem(self, ctx:PartiQLParser.ProjectionItemContext):
        pass

    # Exit a parse tree produced by PartiQLParser#projectionItem.
    def exitProjectionItem(self, ctx:PartiQLParser.ProjectionItemContext):
        pass


    # Enter a parse tree produced by PartiQLParser#setQuantifierStrategy.
    def enterSetQuantifierStrategy(self, ctx:PartiQLParser.SetQuantifierStrategyContext):
        pass

    # Exit a parse tree produced by PartiQLParser#setQuantifierStrategy.
    def exitSetQuantifierStrategy(self, ctx:PartiQLParser.SetQuantifierStrategyContext):
        pass


    # Enter a parse tree produced by PartiQLParser#letClause.
    def enterLetClause(self, ctx:PartiQLParser.LetClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#letClause.
    def exitLetClause(self, ctx:PartiQLParser.LetClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#letBinding.
    def enterLetBinding(self, ctx:PartiQLParser.LetBindingContext):
        pass

    # Exit a parse tree produced by PartiQLParser#letBinding.
    def exitLetBinding(self, ctx:PartiQLParser.LetBindingContext):
        pass


    # Enter a parse tree produced by PartiQLParser#orderByClause.
    def enterOrderByClause(self, ctx:PartiQLParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#orderByClause.
    def exitOrderByClause(self, ctx:PartiQLParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#orderSortSpec.
    def enterOrderSortSpec(self, ctx:PartiQLParser.OrderSortSpecContext):
        pass

    # Exit a parse tree produced by PartiQLParser#orderSortSpec.
    def exitOrderSortSpec(self, ctx:PartiQLParser.OrderSortSpecContext):
        pass


    # Enter a parse tree produced by PartiQLParser#groupClause.
    def enterGroupClause(self, ctx:PartiQLParser.GroupClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#groupClause.
    def exitGroupClause(self, ctx:PartiQLParser.GroupClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#groupAlias.
    def enterGroupAlias(self, ctx:PartiQLParser.GroupAliasContext):
        pass

    # Exit a parse tree produced by PartiQLParser#groupAlias.
    def exitGroupAlias(self, ctx:PartiQLParser.GroupAliasContext):
        pass


    # Enter a parse tree produced by PartiQLParser#groupKey.
    def enterGroupKey(self, ctx:PartiQLParser.GroupKeyContext):
        pass

    # Exit a parse tree produced by PartiQLParser#groupKey.
    def exitGroupKey(self, ctx:PartiQLParser.GroupKeyContext):
        pass


    # Enter a parse tree produced by PartiQLParser#over.
    def enterOver(self, ctx:PartiQLParser.OverContext):
        pass

    # Exit a parse tree produced by PartiQLParser#over.
    def exitOver(self, ctx:PartiQLParser.OverContext):
        pass


    # Enter a parse tree produced by PartiQLParser#windowPartitionList.
    def enterWindowPartitionList(self, ctx:PartiQLParser.WindowPartitionListContext):
        pass

    # Exit a parse tree produced by PartiQLParser#windowPartitionList.
    def exitWindowPartitionList(self, ctx:PartiQLParser.WindowPartitionListContext):
        pass


    # Enter a parse tree produced by PartiQLParser#windowSortSpecList.
    def enterWindowSortSpecList(self, ctx:PartiQLParser.WindowSortSpecListContext):
        pass

    # Exit a parse tree produced by PartiQLParser#windowSortSpecList.
    def exitWindowSortSpecList(self, ctx:PartiQLParser.WindowSortSpecListContext):
        pass


    # Enter a parse tree produced by PartiQLParser#havingClause.
    def enterHavingClause(self, ctx:PartiQLParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#havingClause.
    def exitHavingClause(self, ctx:PartiQLParser.HavingClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#fromClause.
    def enterFromClause(self, ctx:PartiQLParser.FromClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#fromClause.
    def exitFromClause(self, ctx:PartiQLParser.FromClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#whereClauseSelect.
    def enterWhereClauseSelect(self, ctx:PartiQLParser.WhereClauseSelectContext):
        pass

    # Exit a parse tree produced by PartiQLParser#whereClauseSelect.
    def exitWhereClauseSelect(self, ctx:PartiQLParser.WhereClauseSelectContext):
        pass


    # Enter a parse tree produced by PartiQLParser#offsetByClause.
    def enterOffsetByClause(self, ctx:PartiQLParser.OffsetByClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#offsetByClause.
    def exitOffsetByClause(self, ctx:PartiQLParser.OffsetByClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#limitClause.
    def enterLimitClause(self, ctx:PartiQLParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#limitClause.
    def exitLimitClause(self, ctx:PartiQLParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#gpmlPattern.
    def enterGpmlPattern(self, ctx:PartiQLParser.GpmlPatternContext):
        pass

    # Exit a parse tree produced by PartiQLParser#gpmlPattern.
    def exitGpmlPattern(self, ctx:PartiQLParser.GpmlPatternContext):
        pass


    # Enter a parse tree produced by PartiQLParser#gpmlPatternList.
    def enterGpmlPatternList(self, ctx:PartiQLParser.GpmlPatternListContext):
        pass

    # Exit a parse tree produced by PartiQLParser#gpmlPatternList.
    def exitGpmlPatternList(self, ctx:PartiQLParser.GpmlPatternListContext):
        pass


    # Enter a parse tree produced by PartiQLParser#matchPattern.
    def enterMatchPattern(self, ctx:PartiQLParser.MatchPatternContext):
        pass

    # Exit a parse tree produced by PartiQLParser#matchPattern.
    def exitMatchPattern(self, ctx:PartiQLParser.MatchPatternContext):
        pass


    # Enter a parse tree produced by PartiQLParser#graphPart.
    def enterGraphPart(self, ctx:PartiQLParser.GraphPartContext):
        pass

    # Exit a parse tree produced by PartiQLParser#graphPart.
    def exitGraphPart(self, ctx:PartiQLParser.GraphPartContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SelectorBasic.
    def enterSelectorBasic(self, ctx:PartiQLParser.SelectorBasicContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SelectorBasic.
    def exitSelectorBasic(self, ctx:PartiQLParser.SelectorBasicContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SelectorAny.
    def enterSelectorAny(self, ctx:PartiQLParser.SelectorAnyContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SelectorAny.
    def exitSelectorAny(self, ctx:PartiQLParser.SelectorAnyContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SelectorShortest.
    def enterSelectorShortest(self, ctx:PartiQLParser.SelectorShortestContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SelectorShortest.
    def exitSelectorShortest(self, ctx:PartiQLParser.SelectorShortestContext):
        pass


    # Enter a parse tree produced by PartiQLParser#patternPathVariable.
    def enterPatternPathVariable(self, ctx:PartiQLParser.PatternPathVariableContext):
        pass

    # Exit a parse tree produced by PartiQLParser#patternPathVariable.
    def exitPatternPathVariable(self, ctx:PartiQLParser.PatternPathVariableContext):
        pass


    # Enter a parse tree produced by PartiQLParser#patternRestrictor.
    def enterPatternRestrictor(self, ctx:PartiQLParser.PatternRestrictorContext):
        pass

    # Exit a parse tree produced by PartiQLParser#patternRestrictor.
    def exitPatternRestrictor(self, ctx:PartiQLParser.PatternRestrictorContext):
        pass


    # Enter a parse tree produced by PartiQLParser#node.
    def enterNode(self, ctx:PartiQLParser.NodeContext):
        pass

    # Exit a parse tree produced by PartiQLParser#node.
    def exitNode(self, ctx:PartiQLParser.NodeContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeWithSpec.
    def enterEdgeWithSpec(self, ctx:PartiQLParser.EdgeWithSpecContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeWithSpec.
    def exitEdgeWithSpec(self, ctx:PartiQLParser.EdgeWithSpecContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeAbbreviated.
    def enterEdgeAbbreviated(self, ctx:PartiQLParser.EdgeAbbreviatedContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeAbbreviated.
    def exitEdgeAbbreviated(self, ctx:PartiQLParser.EdgeAbbreviatedContext):
        pass


    # Enter a parse tree produced by PartiQLParser#pattern.
    def enterPattern(self, ctx:PartiQLParser.PatternContext):
        pass

    # Exit a parse tree produced by PartiQLParser#pattern.
    def exitPattern(self, ctx:PartiQLParser.PatternContext):
        pass


    # Enter a parse tree produced by PartiQLParser#patternQuantifier.
    def enterPatternQuantifier(self, ctx:PartiQLParser.PatternQuantifierContext):
        pass

    # Exit a parse tree produced by PartiQLParser#patternQuantifier.
    def exitPatternQuantifier(self, ctx:PartiQLParser.PatternQuantifierContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeSpecRight.
    def enterEdgeSpecRight(self, ctx:PartiQLParser.EdgeSpecRightContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeSpecRight.
    def exitEdgeSpecRight(self, ctx:PartiQLParser.EdgeSpecRightContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeSpecUndirected.
    def enterEdgeSpecUndirected(self, ctx:PartiQLParser.EdgeSpecUndirectedContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeSpecUndirected.
    def exitEdgeSpecUndirected(self, ctx:PartiQLParser.EdgeSpecUndirectedContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeSpecLeft.
    def enterEdgeSpecLeft(self, ctx:PartiQLParser.EdgeSpecLeftContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeSpecLeft.
    def exitEdgeSpecLeft(self, ctx:PartiQLParser.EdgeSpecLeftContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeSpecUndirectedRight.
    def enterEdgeSpecUndirectedRight(self, ctx:PartiQLParser.EdgeSpecUndirectedRightContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeSpecUndirectedRight.
    def exitEdgeSpecUndirectedRight(self, ctx:PartiQLParser.EdgeSpecUndirectedRightContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeSpecUndirectedLeft.
    def enterEdgeSpecUndirectedLeft(self, ctx:PartiQLParser.EdgeSpecUndirectedLeftContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeSpecUndirectedLeft.
    def exitEdgeSpecUndirectedLeft(self, ctx:PartiQLParser.EdgeSpecUndirectedLeftContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeSpecBidirectional.
    def enterEdgeSpecBidirectional(self, ctx:PartiQLParser.EdgeSpecBidirectionalContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeSpecBidirectional.
    def exitEdgeSpecBidirectional(self, ctx:PartiQLParser.EdgeSpecBidirectionalContext):
        pass


    # Enter a parse tree produced by PartiQLParser#EdgeSpecUndirectedBidirectional.
    def enterEdgeSpecUndirectedBidirectional(self, ctx:PartiQLParser.EdgeSpecUndirectedBidirectionalContext):
        pass

    # Exit a parse tree produced by PartiQLParser#EdgeSpecUndirectedBidirectional.
    def exitEdgeSpecUndirectedBidirectional(self, ctx:PartiQLParser.EdgeSpecUndirectedBidirectionalContext):
        pass


    # Enter a parse tree produced by PartiQLParser#edgeSpec.
    def enterEdgeSpec(self, ctx:PartiQLParser.EdgeSpecContext):
        pass

    # Exit a parse tree produced by PartiQLParser#edgeSpec.
    def exitEdgeSpec(self, ctx:PartiQLParser.EdgeSpecContext):
        pass


    # Enter a parse tree produced by PartiQLParser#patternPartLabel.
    def enterPatternPartLabel(self, ctx:PartiQLParser.PatternPartLabelContext):
        pass

    # Exit a parse tree produced by PartiQLParser#patternPartLabel.
    def exitPatternPartLabel(self, ctx:PartiQLParser.PatternPartLabelContext):
        pass


    # Enter a parse tree produced by PartiQLParser#edgeAbbrev.
    def enterEdgeAbbrev(self, ctx:PartiQLParser.EdgeAbbrevContext):
        pass

    # Exit a parse tree produced by PartiQLParser#edgeAbbrev.
    def exitEdgeAbbrev(self, ctx:PartiQLParser.EdgeAbbrevContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TableWrapped.
    def enterTableWrapped(self, ctx:PartiQLParser.TableWrappedContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TableWrapped.
    def exitTableWrapped(self, ctx:PartiQLParser.TableWrappedContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TableCrossJoin.
    def enterTableCrossJoin(self, ctx:PartiQLParser.TableCrossJoinContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TableCrossJoin.
    def exitTableCrossJoin(self, ctx:PartiQLParser.TableCrossJoinContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TableQualifiedJoin.
    def enterTableQualifiedJoin(self, ctx:PartiQLParser.TableQualifiedJoinContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TableQualifiedJoin.
    def exitTableQualifiedJoin(self, ctx:PartiQLParser.TableQualifiedJoinContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TableRefBase.
    def enterTableRefBase(self, ctx:PartiQLParser.TableRefBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TableRefBase.
    def exitTableRefBase(self, ctx:PartiQLParser.TableRefBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#tableNonJoin.
    def enterTableNonJoin(self, ctx:PartiQLParser.TableNonJoinContext):
        pass

    # Exit a parse tree produced by PartiQLParser#tableNonJoin.
    def exitTableNonJoin(self, ctx:PartiQLParser.TableNonJoinContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TableBaseRefSymbol.
    def enterTableBaseRefSymbol(self, ctx:PartiQLParser.TableBaseRefSymbolContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TableBaseRefSymbol.
    def exitTableBaseRefSymbol(self, ctx:PartiQLParser.TableBaseRefSymbolContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TableBaseRefClauses.
    def enterTableBaseRefClauses(self, ctx:PartiQLParser.TableBaseRefClausesContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TableBaseRefClauses.
    def exitTableBaseRefClauses(self, ctx:PartiQLParser.TableBaseRefClausesContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TableBaseRefMatch.
    def enterTableBaseRefMatch(self, ctx:PartiQLParser.TableBaseRefMatchContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TableBaseRefMatch.
    def exitTableBaseRefMatch(self, ctx:PartiQLParser.TableBaseRefMatchContext):
        pass


    # Enter a parse tree produced by PartiQLParser#tableUnpivot.
    def enterTableUnpivot(self, ctx:PartiQLParser.TableUnpivotContext):
        pass

    # Exit a parse tree produced by PartiQLParser#tableUnpivot.
    def exitTableUnpivot(self, ctx:PartiQLParser.TableUnpivotContext):
        pass


    # Enter a parse tree produced by PartiQLParser#JoinRhsBase.
    def enterJoinRhsBase(self, ctx:PartiQLParser.JoinRhsBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#JoinRhsBase.
    def exitJoinRhsBase(self, ctx:PartiQLParser.JoinRhsBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#JoinRhsTableJoined.
    def enterJoinRhsTableJoined(self, ctx:PartiQLParser.JoinRhsTableJoinedContext):
        pass

    # Exit a parse tree produced by PartiQLParser#JoinRhsTableJoined.
    def exitJoinRhsTableJoined(self, ctx:PartiQLParser.JoinRhsTableJoinedContext):
        pass


    # Enter a parse tree produced by PartiQLParser#joinSpec.
    def enterJoinSpec(self, ctx:PartiQLParser.JoinSpecContext):
        pass

    # Exit a parse tree produced by PartiQLParser#joinSpec.
    def exitJoinSpec(self, ctx:PartiQLParser.JoinSpecContext):
        pass


    # Enter a parse tree produced by PartiQLParser#joinType.
    def enterJoinType(self, ctx:PartiQLParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by PartiQLParser#joinType.
    def exitJoinType(self, ctx:PartiQLParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by PartiQLParser#expr.
    def enterExpr(self, ctx:PartiQLParser.ExprContext):
        pass

    # Exit a parse tree produced by PartiQLParser#expr.
    def exitExpr(self, ctx:PartiQLParser.ExprContext):
        pass


    # Enter a parse tree produced by PartiQLParser#Intersect.
    def enterIntersect(self, ctx:PartiQLParser.IntersectContext):
        pass

    # Exit a parse tree produced by PartiQLParser#Intersect.
    def exitIntersect(self, ctx:PartiQLParser.IntersectContext):
        pass


    # Enter a parse tree produced by PartiQLParser#QueryBase.
    def enterQueryBase(self, ctx:PartiQLParser.QueryBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#QueryBase.
    def exitQueryBase(self, ctx:PartiQLParser.QueryBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#Except.
    def enterExcept(self, ctx:PartiQLParser.ExceptContext):
        pass

    # Exit a parse tree produced by PartiQLParser#Except.
    def exitExcept(self, ctx:PartiQLParser.ExceptContext):
        pass


    # Enter a parse tree produced by PartiQLParser#Union.
    def enterUnion(self, ctx:PartiQLParser.UnionContext):
        pass

    # Exit a parse tree produced by PartiQLParser#Union.
    def exitUnion(self, ctx:PartiQLParser.UnionContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SfwQuery.
    def enterSfwQuery(self, ctx:PartiQLParser.SfwQueryContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SfwQuery.
    def exitSfwQuery(self, ctx:PartiQLParser.SfwQueryContext):
        pass


    # Enter a parse tree produced by PartiQLParser#SfwBase.
    def enterSfwBase(self, ctx:PartiQLParser.SfwBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#SfwBase.
    def exitSfwBase(self, ctx:PartiQLParser.SfwBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#Or.
    def enterOr(self, ctx:PartiQLParser.OrContext):
        pass

    # Exit a parse tree produced by PartiQLParser#Or.
    def exitOr(self, ctx:PartiQLParser.OrContext):
        pass


    # Enter a parse tree produced by PartiQLParser#ExprOrBase.
    def enterExprOrBase(self, ctx:PartiQLParser.ExprOrBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#ExprOrBase.
    def exitExprOrBase(self, ctx:PartiQLParser.ExprOrBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#ExprAndBase.
    def enterExprAndBase(self, ctx:PartiQLParser.ExprAndBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#ExprAndBase.
    def exitExprAndBase(self, ctx:PartiQLParser.ExprAndBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#And.
    def enterAnd(self, ctx:PartiQLParser.AndContext):
        pass

    # Exit a parse tree produced by PartiQLParser#And.
    def exitAnd(self, ctx:PartiQLParser.AndContext):
        pass


    # Enter a parse tree produced by PartiQLParser#Not.
    def enterNot(self, ctx:PartiQLParser.NotContext):
        pass

    # Exit a parse tree produced by PartiQLParser#Not.
    def exitNot(self, ctx:PartiQLParser.NotContext):
        pass


    # Enter a parse tree produced by PartiQLParser#ExprNotBase.
    def enterExprNotBase(self, ctx:PartiQLParser.ExprNotBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#ExprNotBase.
    def exitExprNotBase(self, ctx:PartiQLParser.ExprNotBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PredicateIn.
    def enterPredicateIn(self, ctx:PartiQLParser.PredicateInContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PredicateIn.
    def exitPredicateIn(self, ctx:PartiQLParser.PredicateInContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PredicateBetween.
    def enterPredicateBetween(self, ctx:PartiQLParser.PredicateBetweenContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PredicateBetween.
    def exitPredicateBetween(self, ctx:PartiQLParser.PredicateBetweenContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PredicateBase.
    def enterPredicateBase(self, ctx:PartiQLParser.PredicateBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PredicateBase.
    def exitPredicateBase(self, ctx:PartiQLParser.PredicateBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PredicateComparison.
    def enterPredicateComparison(self, ctx:PartiQLParser.PredicateComparisonContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PredicateComparison.
    def exitPredicateComparison(self, ctx:PartiQLParser.PredicateComparisonContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PredicateIs.
    def enterPredicateIs(self, ctx:PartiQLParser.PredicateIsContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PredicateIs.
    def exitPredicateIs(self, ctx:PartiQLParser.PredicateIsContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PredicateLike.
    def enterPredicateLike(self, ctx:PartiQLParser.PredicateLikeContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PredicateLike.
    def exitPredicateLike(self, ctx:PartiQLParser.PredicateLikeContext):
        pass


    # Enter a parse tree produced by PartiQLParser#mathOp00.
    def enterMathOp00(self, ctx:PartiQLParser.MathOp00Context):
        pass

    # Exit a parse tree produced by PartiQLParser#mathOp00.
    def exitMathOp00(self, ctx:PartiQLParser.MathOp00Context):
        pass


    # Enter a parse tree produced by PartiQLParser#mathOp01.
    def enterMathOp01(self, ctx:PartiQLParser.MathOp01Context):
        pass

    # Exit a parse tree produced by PartiQLParser#mathOp01.
    def exitMathOp01(self, ctx:PartiQLParser.MathOp01Context):
        pass


    # Enter a parse tree produced by PartiQLParser#mathOp02.
    def enterMathOp02(self, ctx:PartiQLParser.MathOp02Context):
        pass

    # Exit a parse tree produced by PartiQLParser#mathOp02.
    def exitMathOp02(self, ctx:PartiQLParser.MathOp02Context):
        pass


    # Enter a parse tree produced by PartiQLParser#valueExpr.
    def enterValueExpr(self, ctx:PartiQLParser.ValueExprContext):
        pass

    # Exit a parse tree produced by PartiQLParser#valueExpr.
    def exitValueExpr(self, ctx:PartiQLParser.ValueExprContext):
        pass


    # Enter a parse tree produced by PartiQLParser#ExprPrimaryPath.
    def enterExprPrimaryPath(self, ctx:PartiQLParser.ExprPrimaryPathContext):
        pass

    # Exit a parse tree produced by PartiQLParser#ExprPrimaryPath.
    def exitExprPrimaryPath(self, ctx:PartiQLParser.ExprPrimaryPathContext):
        pass


    # Enter a parse tree produced by PartiQLParser#ExprPrimaryBase.
    def enterExprPrimaryBase(self, ctx:PartiQLParser.ExprPrimaryBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#ExprPrimaryBase.
    def exitExprPrimaryBase(self, ctx:PartiQLParser.ExprPrimaryBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#ExprTermWrappedQuery.
    def enterExprTermWrappedQuery(self, ctx:PartiQLParser.ExprTermWrappedQueryContext):
        pass

    # Exit a parse tree produced by PartiQLParser#ExprTermWrappedQuery.
    def exitExprTermWrappedQuery(self, ctx:PartiQLParser.ExprTermWrappedQueryContext):
        pass


    # Enter a parse tree produced by PartiQLParser#ExprTermBase.
    def enterExprTermBase(self, ctx:PartiQLParser.ExprTermBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#ExprTermBase.
    def exitExprTermBase(self, ctx:PartiQLParser.ExprTermBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#nullIf.
    def enterNullIf(self, ctx:PartiQLParser.NullIfContext):
        pass

    # Exit a parse tree produced by PartiQLParser#nullIf.
    def exitNullIf(self, ctx:PartiQLParser.NullIfContext):
        pass


    # Enter a parse tree produced by PartiQLParser#coalesce.
    def enterCoalesce(self, ctx:PartiQLParser.CoalesceContext):
        pass

    # Exit a parse tree produced by PartiQLParser#coalesce.
    def exitCoalesce(self, ctx:PartiQLParser.CoalesceContext):
        pass


    # Enter a parse tree produced by PartiQLParser#caseExpr.
    def enterCaseExpr(self, ctx:PartiQLParser.CaseExprContext):
        pass

    # Exit a parse tree produced by PartiQLParser#caseExpr.
    def exitCaseExpr(self, ctx:PartiQLParser.CaseExprContext):
        pass


    # Enter a parse tree produced by PartiQLParser#values.
    def enterValues(self, ctx:PartiQLParser.ValuesContext):
        pass

    # Exit a parse tree produced by PartiQLParser#values.
    def exitValues(self, ctx:PartiQLParser.ValuesContext):
        pass


    # Enter a parse tree produced by PartiQLParser#valueRow.
    def enterValueRow(self, ctx:PartiQLParser.ValueRowContext):
        pass

    # Exit a parse tree produced by PartiQLParser#valueRow.
    def exitValueRow(self, ctx:PartiQLParser.ValueRowContext):
        pass


    # Enter a parse tree produced by PartiQLParser#valueList.
    def enterValueList(self, ctx:PartiQLParser.ValueListContext):
        pass

    # Exit a parse tree produced by PartiQLParser#valueList.
    def exitValueList(self, ctx:PartiQLParser.ValueListContext):
        pass


    # Enter a parse tree produced by PartiQLParser#sequenceConstructor.
    def enterSequenceConstructor(self, ctx:PartiQLParser.SequenceConstructorContext):
        pass

    # Exit a parse tree produced by PartiQLParser#sequenceConstructor.
    def exitSequenceConstructor(self, ctx:PartiQLParser.SequenceConstructorContext):
        pass


    # Enter a parse tree produced by PartiQLParser#substring.
    def enterSubstring(self, ctx:PartiQLParser.SubstringContext):
        pass

    # Exit a parse tree produced by PartiQLParser#substring.
    def exitSubstring(self, ctx:PartiQLParser.SubstringContext):
        pass


    # Enter a parse tree produced by PartiQLParser#CountAll.
    def enterCountAll(self, ctx:PartiQLParser.CountAllContext):
        pass

    # Exit a parse tree produced by PartiQLParser#CountAll.
    def exitCountAll(self, ctx:PartiQLParser.CountAllContext):
        pass


    # Enter a parse tree produced by PartiQLParser#AggregateBase.
    def enterAggregateBase(self, ctx:PartiQLParser.AggregateBaseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#AggregateBase.
    def exitAggregateBase(self, ctx:PartiQLParser.AggregateBaseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LagLeadFunction.
    def enterLagLeadFunction(self, ctx:PartiQLParser.LagLeadFunctionContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LagLeadFunction.
    def exitLagLeadFunction(self, ctx:PartiQLParser.LagLeadFunctionContext):
        pass


    # Enter a parse tree produced by PartiQLParser#cast.
    def enterCast(self, ctx:PartiQLParser.CastContext):
        pass

    # Exit a parse tree produced by PartiQLParser#cast.
    def exitCast(self, ctx:PartiQLParser.CastContext):
        pass


    # Enter a parse tree produced by PartiQLParser#canLosslessCast.
    def enterCanLosslessCast(self, ctx:PartiQLParser.CanLosslessCastContext):
        pass

    # Exit a parse tree produced by PartiQLParser#canLosslessCast.
    def exitCanLosslessCast(self, ctx:PartiQLParser.CanLosslessCastContext):
        pass


    # Enter a parse tree produced by PartiQLParser#canCast.
    def enterCanCast(self, ctx:PartiQLParser.CanCastContext):
        pass

    # Exit a parse tree produced by PartiQLParser#canCast.
    def exitCanCast(self, ctx:PartiQLParser.CanCastContext):
        pass


    # Enter a parse tree produced by PartiQLParser#extract.
    def enterExtract(self, ctx:PartiQLParser.ExtractContext):
        pass

    # Exit a parse tree produced by PartiQLParser#extract.
    def exitExtract(self, ctx:PartiQLParser.ExtractContext):
        pass


    # Enter a parse tree produced by PartiQLParser#trimFunction.
    def enterTrimFunction(self, ctx:PartiQLParser.TrimFunctionContext):
        pass

    # Exit a parse tree produced by PartiQLParser#trimFunction.
    def exitTrimFunction(self, ctx:PartiQLParser.TrimFunctionContext):
        pass


    # Enter a parse tree produced by PartiQLParser#dateFunction.
    def enterDateFunction(self, ctx:PartiQLParser.DateFunctionContext):
        pass

    # Exit a parse tree produced by PartiQLParser#dateFunction.
    def exitDateFunction(self, ctx:PartiQLParser.DateFunctionContext):
        pass


    # Enter a parse tree produced by PartiQLParser#FunctionCallReserved.
    def enterFunctionCallReserved(self, ctx:PartiQLParser.FunctionCallReservedContext):
        pass

    # Exit a parse tree produced by PartiQLParser#FunctionCallReserved.
    def exitFunctionCallReserved(self, ctx:PartiQLParser.FunctionCallReservedContext):
        pass


    # Enter a parse tree produced by PartiQLParser#FunctionCallIdent.
    def enterFunctionCallIdent(self, ctx:PartiQLParser.FunctionCallIdentContext):
        pass

    # Exit a parse tree produced by PartiQLParser#FunctionCallIdent.
    def exitFunctionCallIdent(self, ctx:PartiQLParser.FunctionCallIdentContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PathStepIndexExpr.
    def enterPathStepIndexExpr(self, ctx:PartiQLParser.PathStepIndexExprContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PathStepIndexExpr.
    def exitPathStepIndexExpr(self, ctx:PartiQLParser.PathStepIndexExprContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PathStepIndexAll.
    def enterPathStepIndexAll(self, ctx:PartiQLParser.PathStepIndexAllContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PathStepIndexAll.
    def exitPathStepIndexAll(self, ctx:PartiQLParser.PathStepIndexAllContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PathStepDotExpr.
    def enterPathStepDotExpr(self, ctx:PartiQLParser.PathStepDotExprContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PathStepDotExpr.
    def exitPathStepDotExpr(self, ctx:PartiQLParser.PathStepDotExprContext):
        pass


    # Enter a parse tree produced by PartiQLParser#PathStepDotAll.
    def enterPathStepDotAll(self, ctx:PartiQLParser.PathStepDotAllContext):
        pass

    # Exit a parse tree produced by PartiQLParser#PathStepDotAll.
    def exitPathStepDotAll(self, ctx:PartiQLParser.PathStepDotAllContext):
        pass


    # Enter a parse tree produced by PartiQLParser#exprGraphMatchMany.
    def enterExprGraphMatchMany(self, ctx:PartiQLParser.ExprGraphMatchManyContext):
        pass

    # Exit a parse tree produced by PartiQLParser#exprGraphMatchMany.
    def exitExprGraphMatchMany(self, ctx:PartiQLParser.ExprGraphMatchManyContext):
        pass


    # Enter a parse tree produced by PartiQLParser#exprGraphMatchOne.
    def enterExprGraphMatchOne(self, ctx:PartiQLParser.ExprGraphMatchOneContext):
        pass

    # Exit a parse tree produced by PartiQLParser#exprGraphMatchOne.
    def exitExprGraphMatchOne(self, ctx:PartiQLParser.ExprGraphMatchOneContext):
        pass


    # Enter a parse tree produced by PartiQLParser#parameter.
    def enterParameter(self, ctx:PartiQLParser.ParameterContext):
        pass

    # Exit a parse tree produced by PartiQLParser#parameter.
    def exitParameter(self, ctx:PartiQLParser.ParameterContext):
        pass


    # Enter a parse tree produced by PartiQLParser#varRefExpr.
    def enterVarRefExpr(self, ctx:PartiQLParser.VarRefExprContext):
        pass

    # Exit a parse tree produced by PartiQLParser#varRefExpr.
    def exitVarRefExpr(self, ctx:PartiQLParser.VarRefExprContext):
        pass


    # Enter a parse tree produced by PartiQLParser#collection.
    def enterCollection(self, ctx:PartiQLParser.CollectionContext):
        pass

    # Exit a parse tree produced by PartiQLParser#collection.
    def exitCollection(self, ctx:PartiQLParser.CollectionContext):
        pass


    # Enter a parse tree produced by PartiQLParser#array.
    def enterArray(self, ctx:PartiQLParser.ArrayContext):
        pass

    # Exit a parse tree produced by PartiQLParser#array.
    def exitArray(self, ctx:PartiQLParser.ArrayContext):
        pass


    # Enter a parse tree produced by PartiQLParser#bag.
    def enterBag(self, ctx:PartiQLParser.BagContext):
        pass

    # Exit a parse tree produced by PartiQLParser#bag.
    def exitBag(self, ctx:PartiQLParser.BagContext):
        pass


    # Enter a parse tree produced by PartiQLParser#tuple.
    def enterTuple(self, ctx:PartiQLParser.TupleContext):
        pass

    # Exit a parse tree produced by PartiQLParser#tuple.
    def exitTuple(self, ctx:PartiQLParser.TupleContext):
        pass


    # Enter a parse tree produced by PartiQLParser#pair.
    def enterPair(self, ctx:PartiQLParser.PairContext):
        pass

    # Exit a parse tree produced by PartiQLParser#pair.
    def exitPair(self, ctx:PartiQLParser.PairContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralNull.
    def enterLiteralNull(self, ctx:PartiQLParser.LiteralNullContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralNull.
    def exitLiteralNull(self, ctx:PartiQLParser.LiteralNullContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralMissing.
    def enterLiteralMissing(self, ctx:PartiQLParser.LiteralMissingContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralMissing.
    def exitLiteralMissing(self, ctx:PartiQLParser.LiteralMissingContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralTrue.
    def enterLiteralTrue(self, ctx:PartiQLParser.LiteralTrueContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralTrue.
    def exitLiteralTrue(self, ctx:PartiQLParser.LiteralTrueContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralFalse.
    def enterLiteralFalse(self, ctx:PartiQLParser.LiteralFalseContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralFalse.
    def exitLiteralFalse(self, ctx:PartiQLParser.LiteralFalseContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralString.
    def enterLiteralString(self, ctx:PartiQLParser.LiteralStringContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralString.
    def exitLiteralString(self, ctx:PartiQLParser.LiteralStringContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralInteger.
    def enterLiteralInteger(self, ctx:PartiQLParser.LiteralIntegerContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralInteger.
    def exitLiteralInteger(self, ctx:PartiQLParser.LiteralIntegerContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralDecimal.
    def enterLiteralDecimal(self, ctx:PartiQLParser.LiteralDecimalContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralDecimal.
    def exitLiteralDecimal(self, ctx:PartiQLParser.LiteralDecimalContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralIon.
    def enterLiteralIon(self, ctx:PartiQLParser.LiteralIonContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralIon.
    def exitLiteralIon(self, ctx:PartiQLParser.LiteralIonContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralDate.
    def enterLiteralDate(self, ctx:PartiQLParser.LiteralDateContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralDate.
    def exitLiteralDate(self, ctx:PartiQLParser.LiteralDateContext):
        pass


    # Enter a parse tree produced by PartiQLParser#LiteralTime.
    def enterLiteralTime(self, ctx:PartiQLParser.LiteralTimeContext):
        pass

    # Exit a parse tree produced by PartiQLParser#LiteralTime.
    def exitLiteralTime(self, ctx:PartiQLParser.LiteralTimeContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TypeAtomic.
    def enterTypeAtomic(self, ctx:PartiQLParser.TypeAtomicContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TypeAtomic.
    def exitTypeAtomic(self, ctx:PartiQLParser.TypeAtomicContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TypeArgSingle.
    def enterTypeArgSingle(self, ctx:PartiQLParser.TypeArgSingleContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TypeArgSingle.
    def exitTypeArgSingle(self, ctx:PartiQLParser.TypeArgSingleContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TypeVarChar.
    def enterTypeVarChar(self, ctx:PartiQLParser.TypeVarCharContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TypeVarChar.
    def exitTypeVarChar(self, ctx:PartiQLParser.TypeVarCharContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TypeArgDouble.
    def enterTypeArgDouble(self, ctx:PartiQLParser.TypeArgDoubleContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TypeArgDouble.
    def exitTypeArgDouble(self, ctx:PartiQLParser.TypeArgDoubleContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TypeTimeZone.
    def enterTypeTimeZone(self, ctx:PartiQLParser.TypeTimeZoneContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TypeTimeZone.
    def exitTypeTimeZone(self, ctx:PartiQLParser.TypeTimeZoneContext):
        pass


    # Enter a parse tree produced by PartiQLParser#TypeCustom.
    def enterTypeCustom(self, ctx:PartiQLParser.TypeCustomContext):
        pass

    # Exit a parse tree produced by PartiQLParser#TypeCustom.
    def exitTypeCustom(self, ctx:PartiQLParser.TypeCustomContext):
        pass



del PartiQLParser