# 知识图谱

> 自动生成的知识关联网络

---

## 统计

| 类型 | 数量 |
|------|------|
| 概念 | 3 |
| 研究主题 | 1 |
| 关联关系 | 7 |

---

## 概念网络

### 概念列表

| 概念 | 关联概念 |
|------|----------|
| 新闻自由 | index, 调查报道 |
| 时代选择 | index |
| 调查报道 | index |

---

## 关联关系

- 新闻自由 ←→ index
- 新闻自由 ←→ 调查报道
- 时代选择 ←→ index
- 调查报道 ←→ index
- 新闻自由 → 媒体与权力 (研究主题)
- 时代选择 → 媒体与权力 (研究主题)
- 调查报道 → 媒体与权力 (研究主题)

---

## 图谱数据

```json
{
  "nodes": [
    {
      "id": "新闻自由",
      "label": "新闻自由",
      "type": "concept"
    },
    {
      "id": "时代选择",
      "label": "时代选择",
      "type": "concept"
    },
    {
      "id": "调查报道",
      "label": "调查报道",
      "type": "concept"
    },
    {
      "id": "媒体与权力",
      "label": "媒体与权力",
      "type": "topic"
    }
  ],
  "edges": [
    {
      "from": "新闻自由",
      "to": "index",
      "type": "concept_to_concept"
    },
    {
      "from": "新闻自由",
      "to": "调查报道",
      "type": "concept_to_concept"
    },
    {
      "from": "时代选择",
      "to": "index",
      "type": "concept_to_concept"
    },
    {
      "from": "调查报道",
      "to": "index",
      "type": "concept_to_concept"
    },
    {
      "from": "新闻自由",
      "to": "媒体与权力",
      "type": "concept_to_topic"
    },
    {
      "from": "时代选择",
      "to": "媒体与权力",
      "type": "concept_to_topic"
    },
    {
      "from": "调查报道",
      "to": "媒体与权力",
      "type": "concept_to_topic"
    }
  ]
}
```

---

*图谱自动生成于 2026-03-15*
